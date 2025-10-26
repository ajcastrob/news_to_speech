import hashlib
from newspaper import Article
import json
import re
import nltk
import os


# Esto para la descarga autmática de la noticia.
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")


# Crear una función que limpie el nombre para usarlo
def clean_name(filename: str):
    """Limpia el título del artículo para usarlo en el archivo json"""
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    filename = filename.strip().replace(
        " ", "_"
    )  # Reemplazar los expacios y caracteres.
    return filename[:50]  # Para evitar que título sea muy largo


def extract_article(url):
    """Descargar y parsear un artículo dado su URL
    y devuelve un diccionario.
    output: título, autores, fecha de publicación, texto.
    """
    try:
        # Instanciar el objeto.
        article = Article(url, language="es")
        # Descargar.
        article.download()
        article.parse()
        article.nlp()

        # Generar un hash para guardar en json
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]

        # Llamar a la función que usa el título
        safe_title = clean_name(article.title) or "sin_titulo"

        # Crear el nombre único para el json
        filename = f"{safe_title}_{url_hash}.json"

        # Crear el diccionar con los datos:
        noticia = {
            "título": article.title,
            "autores": ", ".join(article.authors) if article.authors else "Desconocido",
            "fecha de publicación": str(article.publish_date),
            "texto": article.text,
        }

        return noticia, filename
    except (TypeError, AttributeError) as e:
        print(f"Error: url inválido: {e}")
        return None, None


def save_article(article, filename, folder="articulos"):
    # Guardamos el archivo:
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(article, file, ensure_ascii=False, indent=4)

    print("Artículo guardado con éxito")


with open("noticias.json", "r") as file:
    data = json.load(file)
    data[0]["Categoría"]
    url = data[0]["URL"]

print(url)
data_noticia, filename = extract_article(url)
save_article(data_noticia, filename)
