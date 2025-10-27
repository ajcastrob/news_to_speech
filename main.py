from classify_news import run_classification
from news import process_article
from text_to_speach import run_tts_on_articles


def main(url, analysis_limit=100, top_n=5):
    if url:
        get_news = run_classification(url, analysis_limit=analysis_limit, top_n=top_n)

        if not get_news:
            print("No se encontraro noticias relevantes.")
            return None

        lista_path_news = process_article(get_news)
        run_tts_on_articles(lista_path_news)
    else:
        print("Ingrese un URL válido")
        return None

    return lista_path_news


if __name__ == "__main__":
    print("Ingrese el URL del portal de noticias: ")
    portal = input()
    path = main(portal, analysis_limit=100, top_n=5)
