
lis = [
    {
        "id": 94362,
        "titulo": "Ba\u00f1eros 1 boca",
        "duracion": 97,
        "genero": [
            "Comedia"
        ],
        "sinopsis": "Un grupo de hombres que eran ba\u00f1eros en la playa.",
        "pais_de_origen": "Argentina",
        "idioma": "Castellano",
        "clasificacion": [
            "PG-13"
        ],
        "calificacion": 0,
        "disponible": True
    },
    {
        "id": 28062,
        "titulo": "Papa se volvio loco boca",
        "duracion": 90,
        "genero": [
            "Comedia"
        ],
        "sinopsis": "Una pareja que tiene una nueva luna de miel.",
        "pais_de_origen": "Argentina",
        "idioma": "Castellano",
        "clasificacion": [
            "ATP"
        ],
        "calificacion": 0,
        "disponible": True
    }
]



while True:
    titu = input("ingrese el titulo: ")
    for x in lis:
        if titu in x['titulo'] :
            print(x)
            False
        else:
            print(f"{titu} no está en la lista de pelis")
            break
    break
        
# while True:
#     titulo_buscado = input("Ingrese el titulo de la pelicula que desee buscar: ")
#     for pelicula in lista_peliculas:    
#         if titulo_buscado in pelicula['titulo']:
#             print(pelicula)

