import newspaper


def get_news_url(source_url):
    # Contruir una lista con los periódicos
    urls = []
    try:
        # Instanciar el objeto.
        paper = newspaper.build(source_url, memoize_articles=False)
        for article in paper.articles:
            urls.append(article.url)

    except Exception as e:
        print(f"Error al procesar el periódico desde {source_url}: {e}")
        return []

    print(f"Se encontraron {len(urls)} artículos en {source_url}")
    return urls
