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


def clarify_news(data_news):
    # Definir el modelo
    model = genai.GenerativeModel("gemini-2.5-flash")

    results = []

    for item in data_news[:20]:
        url = item

        prompt = f"""
Clasifica esta noticia según su URL

    Devuelve **solo** un JSON con el formato exacto:
    {{
      "Categoría": "...",
      "URL": "{url}"
    }}
    """

        try:
            response = model.generate_content(prompt)
            text = response.text.strip()
            parsed = extract_json(text)
            if parsed:
                results.append(parsed)
            else:
                print(f"Respuesta no válida para {url}")
                results.append({"Categoría": "Desconocido", "URL": url})
        except Exception as e:
            print(f"Error procesando {url}: {e}")

        time.sleep(1)

    return results


portal = "https://www.elnacional.com"
news = get_news_url(portal)
classified_news = clarify_news(news)

with open("noticias.json", "w", encoding="utf-8") as file:
    json.dump(classified_news, file, ensure_ascii=False, indent=2)
