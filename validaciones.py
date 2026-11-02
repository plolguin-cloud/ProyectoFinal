# Validaciones de lo que escribe el usuario


def texto_valido(texto):
    """True si el usuario escribió algo (no está vacío)."""
    return len(texto.strip()) > 0


def es_numero(texto):
    """True si el texto se puede convertir en número (ej: '7.5')."""
    try:
        float(texto)
        return True
    except ValueError:
        return False