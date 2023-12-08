import json
import random

# Alta, baja, modificación de pelicula
def ABM_peliculas():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        alta()
    elif opcion_submenu == "2":
        print(opcion2_submenu_1)
        modificacion_pelicula_existente()
    elif opcion_submenu == "3":
        print(opcion3_submenu_1)
        baja_pelicula()
    elif opcion_submenu == "4":
        return
    else:
        print("Opción incorrecta, vuelva a ingresar una opción")
        ABM_peliculas()

# Calificacion de titulos
def calificacion_titulos():
    contador = 0
    lis = []
    while contador < 10:
        for peliculas in random.choices(lista_peliculas):
                print(peliculas)
                
                #lis.append[peliculas] #HACER PARA QUE NO SE REPITA LA MISMA PELICULA
                # ESTO DE QUE NO SE REPITA TIENE QUE HACERSE EN EL ALTA CON LA ID
                while True:
                    desea = input("Desea calificar la pelicula? S/N: ")
                    if desea == "S":
                        new_calificacion = int(input("Ingrese la nueva calificacion del 1 al 10: "))
                        contador += 1
                        if peliculas["calificacion"] == 0:
                            peliculas["calificacion"] = new_calificacion
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                        else:
                            peliculas["calificacion"] = (peliculas["calificacion"]+new_calificacion)/2
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                    elif desea == "N":
                        contador += 1
                        break
                    else:
                        print("Opción incorrecta, ingrese S/N")
                        continue
                        
# Reportes y estadisticas
def reportes_estadisticas():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        listado_pelicula()
    elif opcion_submenu == "2":
        pelicula_mayor_puntaje()
    elif opcion_submenu == "3":
        porcentaje_disponible(lista_peliculas)
    elif opcion_submenu == "4":
        return
    else:
        reportes_estadisticas()

# Imprime lista de generos
def imprimir_generos(generos_disponibles):
        print("Generos disponibles para la pelicula: ")
        for x in range(0, len(generos_disponibles)):
            print(f" - {generos_disponibles[x]}")

# Abre y lee el archivo
def leer_archivo(nombre_archivo):
        with open(nombre_archivo, 'r') as conexion:
            return json.load(conexion)

# Graba las modificaciones en el archivo
def grabar_archivo(lista_peliculas, nombre_archivo):
        with open(nombre_archivo, "w") as conexion:
            json.dump(lista_peliculas, conexion, indent=4)

# Sistema para dar de alta
def alta():
        lista_peliculas = leer_archivo("peliculasNew.json")
        generos_disponibles = ["Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica"]
        clasificacion = ["ATP" , "PG" , "PG-13" , "R", "NC-17"]
        clasificacion_vacio = []

        id_pelicula = random.randint(10000, 99999)
        titulo = input("Ingrese el titulo de la pelicula: ")
        generos = []
        imprimir_generos(generos_disponibles)   

        while True:
            rta_genero = input("Ingrese un genero para la pelicula: ")
            if rta_genero in generos_disponibles:
                generos.append(rta_genero)
            else:
                print("Ingrese un genero valido...")
                imprimir_generos(generos_disponibles)
                continue
            continua = input("Desea agregar otro genero?: (S/N)")
            if continua == "N":
                break
            elif continua == "S":
                continue
            else:
                print("Opcion incorrecta")
                continua = input("Desea agregar otro genero?: (S/N)")
                if continua == "N":
                    break
                elif continua == "S":
                    continue
        
        while True:
            try:
                duracion = int(input("Ingrese la duracion de la pelicula en minutos: "))
                break
            except:
                print("Duración invalida, ingrese números")
                continue
                
        sinopsis = input("Escriba una sinopsis de la pelicula: ")
        pais_de_origen = input("Ingrese el país de origen de la pelicula: ")
        idioma = input("Ingrese el idioma de la pelicula: ")
        while True:
            print(f"Elija una de estas posibles clasificaciones: {clasificacion}")
            clasificacion_ingresada = input("Ingrese una clasificación: ")
            if clasificacion_ingresada in clasificacion:
                clasificacion_vacio.append(clasificacion_ingresada)
            elif clasificacion_ingresada not in clasificacion:
                print("Opción invalida, elija una clasificación valida")
                continue
            break
        while True:
            calificacion = 0
            disponible = input("La pelicula está disponible? S/N: ")
            if disponible == "S":
                disponible = True
                break
            elif disponible == "N":
                disponible = False
                break
            else:
                print("Opción invalida, ingrese una opción valida")
                

        peliculas_a_agregar = {
            "id": id_pelicula,
            "titulo": titulo,
            "duracion": duracion,
            "genero": generos,
            "sinopsis": sinopsis,
            "pais_de_origen": pais_de_origen,
            "idioma": idioma,
            "clasificacion": clasificacion_vacio,
            "calificacion": calificacion,
            "disponible": disponible
        }

        lista_peliculas.append(peliculas_a_agregar)
        grabar_archivo(lista_peliculas, "peliculasNew.json")
        print("Película agregada exitosamente.")         

# Busca pelicula por id (Y las modifica)
def buscar_titulo_id():
    lista_peliculas = leer_archivo("peliculasNew.json")
    while True:
        id_buscado = int(input("Ingrese id:"))
        for pelicula in lista_peliculas:
            if pelicula['id'] == id_buscado:
                print(pelicula)
                posicion = lista_peliculas.index(pelicula)
                print(posicion)
                desea = input("Que desea modificar?: ")
                if desea == "titulo":
                    new_titulo = input("Ingrese el nuevo titulo: ")
                    lista_peliculas[posicion]["titulo"] = new_titulo
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "duracion":
                    new_duracion = int(input("Ingrese la nueva duracion: "))
                    lista_peliculas[posicion]["duracion"] = new_duracion #INDEX 
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "genero":
                    generos_disponibles = ["Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica"]
                    generos = []
                    imprimir_generos(generos_disponibles)   
                    while True:
                        rta_genero = input("Ingrese un genero para la pelicula: ")
                        if rta_genero in generos_disponibles:
                            generos.append(rta_genero)
                        else:
                            print("Ingrese un genero valido...")
                            imprimir_generos(generos_disponibles)
                            continue
                        continua = input("Desea agregar otro genero?: (S/N)")
                        if continua == "N":
                            break
                        elif continua == "S":
                            continue
                        else:
                            print("Opcion incorrecta")
                            continua = input("Desea agregar otro genero?: (S/N)")
                            if continua == "S":
                                continue
                            elif continua == "N":
                                break
                            else:
                                print("Opcion incorrecta")
                                continue        
                    lista_peliculas[posicion]["genero"] = generos
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")

                elif desea == "sinopsis":
                    new_sinopsis = input("Ingrese la nueva sinopsis: ")
                    lista_peliculas[posicion]["sinopsis"] = new_sinopsis
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "pais de origen":
                    new_pais = input("Ingrewse el nuevo país de origen: ")
                    lista_peliculas[posicion]["pais_de_origen"] = new_pais
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "idioma":
                    new_idioma = input("Ingrese el nuevo idioma: ")
                    lista_peliculas[posicion]["idioma"] = new_idioma
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "clasificacion":
                    new_clasificacion = input("Ingrese la nueva clasificacion: ")
                    lista_peliculas[posicion]["clasificacion"] = new_clasificacion
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "calificacion":
                    print("hacer")
                elif desea == "disponible":
                    while True:
                        new_disponible = input("Está disponible la pelicula? S/N: ")
                        if new_disponible == "S":
                            lista_peliculas[posicion]["disponible"] = True
                            print(pelicula)
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                        elif new_disponible == "N":
                            lista_peliculas[posicion]["disponible"] = False
                            print(pelicula)
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                        else:
                            print("La opción ingresada es incorrecta")

                #
        else:
            print("El titulo de la pelicula es incorrecto")
            continue
        
# Busca pelicula por titulo (Y las modifica)
def buscar_pelicula_titulo(lista_peliculas):
    lista_peliculas = leer_archivo("peliculasNew.json")
    boca()
    while True:
        titulo_seleccionado = input("Ingrese el titulo que desea modificar: ")
        for pelicula in lista_peliculas:
            # QUE EL USUSARIO ELIJA UNA PELICULA
            if titulo_seleccionado == pelicula['titulo']:
                print(pelicula)
                posicion = lista_peliculas.index(pelicula)
                print(posicion)
                desea = input("Que desea modificar?: ")
                if desea == "titulo":
                    new_titulo = input("Ingrese el nuevo titulo: ")
                    lista_peliculas[posicion]["titulo"] = new_titulo
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "duracion":
                    new_duracion = int(input("Ingrese la nueva duracion: "))
                    lista_peliculas[posicion]["duracion"] = new_duracion #INDEX 
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "genero":
                    generos_disponibles = ["Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica"]
                    generos = []
                    imprimir_generos(generos_disponibles)   
                    while True:
                        rta_genero = input("Ingrese un genero para la pelicula: ")
                        if rta_genero in generos_disponibles:
                            generos.append(rta_genero)
                        else:
                            print("Ingrese un genero valido...")
                            imprimir_generos(generos_disponibles)
                            continue
                        continua = input("Desea agregar otro genero?: (S/N)")
                        if continua == "N":
                            break
                        elif continua == "S":
                            continue
                        else:
                            print("Opcion incorrecta")
                            continua = input("Desea agregar otro genero?: (S/N)")
                            if continua == "S":
                                continue
                            elif continua == "N":
                                break
                            else:
                                print("Opcion incorrecta")
                                continue        
                    lista_peliculas[posicion]["genero"] = generos
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")

                elif desea == "sinopsis":
                    new_sinopsis = input("Ingrese la nueva sinopsis: ")
                    lista_peliculas[posicion]["sinopsis"] = new_sinopsis
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "pais de origen":
                    new_pais = input("Ingrewse el nuevo país de origen: ")
                    lista_peliculas[posicion]["pais_de_origen"] = new_pais
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "idioma":
                    new_idioma = input("Ingrese el nuevo idioma: ")
                    lista_peliculas[posicion]["idioma"] = new_idioma
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "clasificacion":
                    new_clasificacion = input("Ingrese la nueva clasificacion: ")
                    lista_peliculas[posicion]["clasificacion"] = new_clasificacion
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "calificacion":
                    print("hacer")
                elif desea == "disponible":
                    while True:
                        new_disponible = input("Está disponible la pelicula? S/N: ")
                        if new_disponible == "S":
                            lista_peliculas[posicion]["disponible"] = True
                            print(pelicula)
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                        elif new_disponible == "N":
                            lista_peliculas[posicion]["disponible"] = False
                            print(pelicula)
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                        else:
                            print("La opción ingresada es incorrecta")
                break          
            else:
                print("no funciona")
        
                
def boca():
    lista_peliculas = leer_archivo("peliculasNew.json")

    while True:
        titu = input("ingrese el titulo: ")
        for x in lista_peliculas:
            if titu in x['titulo']:
                print(f"Titulos encontrados para modificar: {x['titulo']}")
                False
        break
        
# Modifica pelicula existente (MENTIRA, ESTO ESTÁ DE MÁS(No modifica nada y solo te manda al sistema de busqueda donde modifica))
def modificacion_pelicula_existente():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        buscar_titulo_id()
    elif opcion_submenu == "2":
        buscar_pelicula_titulo(lista_peliculas)
    elif opcion_submenu == "3":
        print(submenu_1)
        ABM_peliculas()
    else:
        modificacion_pelicula_existente()

# Da de baja la pelicula por id
def baja_id():
    while True:
        id_buscado = int(input("Ingrese el id de la pelicula que desee eliminar: "))
        for pelicula in lista_peliculas:
            if pelicula["id"] == id_buscado:
                print(pelicula)
                posicion = lista_peliculas.index(pelicula)
                lista_peliculas.pop(posicion)
                print("La pelicula ha sido eliminada correctamente")
                grabar_archivo(lista_peliculas, "peliculasNew.json")
                break
        
# Da de baja la pelicula por titulo
def baja_titulo():
    while True:
        titulo_buscado = input("Ingrese el titulo de la pelicula que desee eliminar: ")
        for pelicula in lista_peliculas:
            if pelicula["titulo"] == titulo_buscado:
                print(pelicula)
                posicion = lista_peliculas.index(pelicula)
                lista_peliculas.pop(posicion)
                print("La pelicula ha sido eliminada correctamente")
                grabar_archivo(lista_peliculas, "peliculasNew.json")
                break

# Sistema de baja de pelis (No da de baja nada y te manda a la baja de pelis por id y titulo)
def baja_pelicula():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        baja_id()
    elif opcion_submenu == "2":
        baja_titulo()
    elif opcion_submenu == "3":
        print(volver)
    else:
        baja_pelicula() 

# Sistema de menu inicio
def menu_inicio():
    while True:
        print(menu)
        opcionUsuario = input("ingrese la opcion que desea :")
        if opcionUsuario == "1":
            print(submenu_1)
            ABM_peliculas()
        elif opcionUsuario == "2":
            calificacion_titulos()
        elif opcionUsuario == "3":
            print(submenu_3)
            reportes_estadisticas()
        elif opcionUsuario == "4":
            pregunta = input("Realmente desea salir? S/N: ")
            if pregunta == "S":
                print("Saliste del programa, Muchas gracias por utilizar CINEMA+")
                break
            elif pregunta == "N":
                continue
            else:
                print("Opción incorrecta")
                continue
        else:
            print("opción invalida")
            continue
        
# Sistema para mostrar un listado de peliculas(titulo, genero, calificacion) ordenado por titulo
def listado_pelicula():
    lista_peliculas = leer_archivo("peliculasNew.json")
    lista_peliculas.sort(key=lambda x: x["titulo"])
    for pelicula in lista_peliculas:
        print(f' \n Pelicula : {pelicula["titulo"]} \n Genero: {pelicula["genero"]}, \n Calificacion:  {pelicula["calificacion"]}')
    
# Sistema para mostrar un listado de 15 peliculas(titulo, genero, calificacion) ordenado por calificacion de mayor puntaje
# ESTÁ MAL.... LA CONSIGNA PIDE OTRA COSA
def pelicula_mayor_puntaje():
    lista_peliculas = leer_archivo("peliculasNew.json")
    lista_peliculas.sort(key=lambda x: x["calificacion"])
    lista_peliculas.reverse()
    for pelicula in lista_peliculas:
        print(f' \n Pelicula : {pelicula["titulo"]} \n Genero: {pelicula["genero"]}, \n Calificacion:  {pelicula["calificacion"]}')

# Muestra cantidad de peliculas, un histograma y porcentaje de cantidad de peliculas 
def porcentaje_disponible(lista_peliculas):
    lista_peliculas = leer_archivo("peliculasNew.json")
    print(f"La totalidad de peliculas cargadas son {len(lista_peliculas)}")
    disponibles = 0
    for x in lista_peliculas:
        if x ["disponible"] == True:
            disponibles +=1
    porcentaje_disponible = round(((disponibles)*100)/len(lista_peliculas))
    peli_disponible = (round(porcentaje_disponible))
    print(f"El porcentaje de peliculas disponibles es {porcentaje_disponible}%")
    print("*" * peli_disponible)
    no_disponibles = 0
    for x in lista_peliculas:
        if x["disponible"] == False:
            no_disponibles +=1
    porcentaje_no_disp = round(((no_disponibles)*100)/len(lista_peliculas))
    peli_no_disp = (round(porcentaje_no_disp))
    print(f"El procentaje de peliculas no disponibles es {porcentaje_no_disp}%")
    print("*" * peli_no_disp)


#TODO
menu = "CINEMA+ \n 1. ABM de películas \n 2. Calificación de títulos \n 3. Reportes y estadísticas \n 4. Salir"
submenu_1 = "CINEMA+ \n Alta, Baja y modificación de películas \n 1. Alta de nueva película \n 2. Modificación de película existente \n 3. Baja de película (eliminar) \n 4. Volver"
opcion2_submenu_1 = "CINEMA+ \n Modificar película existente \n 1. Buscar por id \n 2. Buscar por titulo \n 3. Volver"
opcion3_submenu_1 = "CINEMA+ \n Eliminar una película existente \n 1. Buscar por id \n 2. Buscar por titulo \n 3. Volver"
volver = "Volver"
submenu_2 = "CALIFICACION DE TITULOS"
submenu_3 = "CINEMA+ \n Reportes y estadísticas \n 1. Listado de películas \n 2. Películas de mayor puntaje \n 3. Porcentaje de películas disponibles en la plataforma \n 4. Volver"
lista_peliculas = leer_archivo("peliculasNew.json")


#WHILE
while True:
    print(menu)
    opcionUsuario = input("ingrese la opcion que desea :")
    if opcionUsuario == "1":
        print(submenu_1)
        ABM_peliculas()
    elif opcionUsuario == "2":
        print(submenu_2)
        calificacion_titulos()
    elif opcionUsuario == "3":
        print(submenu_3)
        reportes_estadisticas()
    elif opcionUsuario == "4":
        pregunta = input("Realmente desea salir? S/N: ")
        if pregunta == "S":
            print("Saliste del programa, Muchas gracias por utilizar CINEMA+")
            break
        elif pregunta == "N":
            continue
        else:
            print("Opción incorrecta")
            continue
    else:
        print("opción invalida")
        continue

# DETALLES:
#   En alta de pelicula en el país de origen y el idioma se puede ingresar cualquier cosa.