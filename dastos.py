# Lectura del archivo JSON
import json


def cargar(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se pudo leer el archivo", archivo)
        return []

    h
