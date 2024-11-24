def sanitizar_entrada(texto):
    """
    Limpia y normaliza la entrada eliminando espacios, pasando a minúsculas y
    reemplazando caracteres acentuados.
    """
    texto = texto.lower().strip()
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u"
    }
    for acento, reemplazo in reemplazos.items():
        texto = texto.replace(acento, reemplazo)
    return texto
