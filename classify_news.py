from import_news import get_news_url
import google.generativeai as genai
import json
import re
import time
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.configure(api_key=api_key)


def extract_json(text):
    # Extrae un bloque de Json válido para Gemini
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            return None
    except json.JSONDecodeError:
        return None


def clarify_news(data_news, top_n=5):
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Unir todas las URLs en un solo string, una por línea. Hago compresión de lista.
    url_list_str = "\n".join([f"- {url}" for url in data_news])

    prompt = f"""
Eres un analista de noticias experto. Tu tarea es identificar las {top_n} noticias más relevantes
      de la siguiente lista de URLs.
 
 **Instrucciones:**
 
1.  **Analiza la lista de URLs**: Revisa la siguiente lista de artículos de noticias.
2.  **Evalúa la Relevancia**: Determina la importancia de cada noticia. Considera factores como el
      impacto global, la actualidad, la originalidad y la trascendencia del tema.
3.  **Selecciona el Top {top_n}**: Escoge las {top_n} noticias más importantes y relevantes.
4.  **Genera el Resultado**: Devuelve **únicamente** un objeto JSON que contenga una lista llamada
      "noticias_relevantes". Cada objeto en la lista debe tener el siguiente formato exacto:
    {{
      "Categoría": "...",
     "Relevancia": <puntuación del 1 al 10>,
     "URL": "..."
   }}

**Lista de URLs a analizar:**
{url_list_str}
 Por favor, asegúrate de devolver solo el objeto JSON y nada más.
"""

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        # Llamar a la función json.
        parsed = extract_json(text)

        if parsed and "noticias_relevantes" in parsed:
            return parsed["noticias_relevantes"]
        else:
            print(f"Error procesando lista")
            return []
    except Exception as e:
        print(f"Error procesando url {e}")
        return []


def run_classification(portal_url, analysis_limit=100, top_n=5):
    """Ejecuta el proceso de clasificación por lote de noticias"""

    print(f"Iniciando la obtención desde {portal_url}")
    all_news_url = get_news_url(portal_url)

    # Limitar la cantidad de URl analizar sin exceder el límite
    urls_to_analyze = all_news_url[:analysis_limit]

    print(f"Enviando {len(urls_to_analyze)} noticias a Gemini")
    classified_news = clarify_news(urls_to_analyze, top_n=top_n)

    if classified_news:
        print(
            f"Clasificación completada. Se recibieron las {len(classified_news)} más relevantes"
        )

    else:
        print("No se recibieron noticias relevantes")

    return classified_news
