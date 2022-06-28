import webbrowser


def buscar_lo_seleccionado(query:str):
    '''
    Description:
        Searching in the browser

    Args:
        query:str: what you wanna find

    '''
    search_engines = {"https://google.com/search?q={}", "https://scholar.google.es/scholar?hl=es&as_sdt=0%2C5&q={}&btnG=", "https://duckduckgo.com/?q={}"}

    for url in search_engines:
        webbrowser.open(url.format(query), new=2, autoraise=True)

