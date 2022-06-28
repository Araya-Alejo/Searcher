import webbrowser


def buscar_lo_seleccionado(query:str):
    '''
    Description:
        Searching in the browser

    Args:
        query:str: what you wanna find

    '''
    webbrowser.open("https://google.com/search?q={}".format(query), new=2, autoraise=True)

