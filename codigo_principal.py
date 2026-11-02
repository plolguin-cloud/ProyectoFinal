from datos import cargar
from diccionarios import MENU, CAMPOS_TEXTO
from validaciones import texto_valido, es_numero
from consultas import buscar_texto, puntaje_minimo, ordenar


def mostrar(resultados):
    if not resultados:
        print("Sin resultados.")
    for p in resultados:
        print(f"- {p['titulo']} ({p['año']}) | {p['genero']} | puntaje {p['puntaje']}")


def main():
    peliculas = cargar("peliculas.json")
    while True:
        print()
        for clave, texto in MENU.items():
            print(f"{clave}) {texto}")
        opcion = input("Elegí una opción: ")

        if opcion in CAMPOS_TEXTO:  
            texto = input("Texto a buscar: ")
            if texto_valido(texto):
                mostrar(buscar_texto(peliculas, CAMPOS_TEXTO[opcion], texto))
            else:
                print("No escribiste nada.")
        elif opcion == "3":
            minimo = input("Puntaje mínimo: ")
            if es_numero(minimo):
                mostrar(puntaje_minimo(peliculas, float(minimo)))
            else:
                print("Ingresá un número.")
        elif opcion == "4":
            mostrar(ordenar(peliculas, "puntaje"))
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


main()
