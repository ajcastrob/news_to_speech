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


def process_article(clasified_news: list):
    """Procesa las noticias clasificadas, extrañendo y guardando cada una
    output: una lista de strings con la ruta de los archivos guardados.
    """
    # Crear la lista vacía.
    save_path_article = []
    # Crear una muetra de la totalidad de los artículos.
    total_article = len(clasified_news)

    # Hacer el bucle.
    for i, news_item in enumerate(clasified_news, 1):
        # Buscar en el diccionario el url
        url = news_item.get("URL")
        if not url:
            print(f"El item {i} no tiene URL válido. Se salta.")
            continue

        print(f"Procesando artículo {i}/{total_article} : {url}")
        # LLamar a la función que extrae el artículo
        article_data, filename = extract_article(url)

        # Guardar el artículo.
        if article_data and filename:
            save_article(article_data, filename)
            filepath = os.path.join("articulos", filename)
            # Guardo los path en la lista.
            save_path_article.append(filepath)
        else:
            print(f"No se pudo guardar el artículo {i} dese {url}")

    print("Procesado de artículos completo")
    return save_path_article
