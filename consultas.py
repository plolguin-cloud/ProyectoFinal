# Consultas sobre la lista de películas (cada película es un diccionario)


def buscar_texto(peliculas, campo, texto):
    return [p for p in peliculas if texto.lower() in str(p.get(campo, "")).lower()]


def puntaje_minimo(peliculas, minimo):
    return [p for p in peliculas if p.get("puntaje", 0) >= minimo]


def ordenar(peliculas, campo, descendente=True):
    return sorted(peliculas, key=lambda p: p.get(campo, 0), reverse=descendente)
