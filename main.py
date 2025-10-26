from classify_news import run_classification
from news import process_article
from text_to_speach import run_tts_on_articles


def main(url, items=5):
    if url:
        get_news = run_classification(url, items)
        lista_path_news = process_article(get_news)
    else:
        print("Ingrese un Url")
        return None

    return lista_path_news


if __name__ == "__main__":
    print("Ingrese el nombre del portal de noticias: ")
    portal = input()
    path = main(portal, 2)
    run_tts_on_articles(path)
