print(" - - - - - - - - - - - MENU - - - - - - - - - - -\n"
      f"1.  CREAR GRUPO ARTEMIS:\n"
      f"1.l LISTAR CAMPERS DE ARTEMIS\n"
      f"1.2 AGREGAR CAMPERS A ARTEMIS\n"
      f"1.3 ELIMINAR CAMPERS DE ARTEMIS\n"
      f"1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS\n"
      f"1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS\n"
      f"2.  CREAR GRUPO SPUTNIK:\n"
      f"2.1 LISTAR CAMPERS DE SPUTNIK:\n"
      f"2.2 AGREGAR CAMPERS A SPUTNIK\n"
      f"2.3 ELIMINAR CAMPERS DE SPUTNIK\n"
      f"2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK\n"
      f"2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK\n")
a = True
while a == True:
    opcion = str(input("Digite opción: "))
    if opcion == "1.1":
        campers_artemis = []
    elif opcion == "1.2":
        while True:
            campers_a = str(input("Agregue un camper a Artemis:\n| "))
            campers_artemis.append(campers_a)
            seguir = str(input("Desea seguir agregando campers?\nMarque 1 para si\nMarque 2 para no\n| "))
            if seguir == "2":
                break
    elif opcion == "1.3":
        eliminar = str(input("Digite el nombre del camper de Artemis que desea eliminar:\n| "))
        campers_artemis.remove(eliminar)
    elif opcion == "1.4":
        campers_artemis.sort()
    elif opcion == "1.5":
        buscar = str(input("Ingrese el nombre del camper que desea buscar:\n|"))
        print(f"El camper que buscar se encuentra en la pocisión {campers_artemis.index(buscar)} de la lista de artemis")
    elif opcion == "2.1":
        campers_sputnik = []
    elif opcion == "2.2":
        while True:
            campers_s = str(input("Agregue un camper a Sputnik:\n| "))
            campers_sputnik.append(campers_s)
            seguir = str(input("Desea seguir agregando campers?\nMarque 1 para si\nMarque 2 para no\n| "))
            if seguir == "2":
                break
    elif opcion == "2.3":
        eliminar = str(input("Digite el nombre del camper de sputnik que desea eliminar:\n| "))
        campers_sputnik.remove(eliminar)
    elif opcion == "2.4":
        campers_sputnik.sort()
    elif opcion == "2.5":
        buscar = str(input("Ingrese el nombre del camper que desea buscar:\n|"))
        print(f"El camper que buscar se encuentra en la pocisión {campers_sputnik.index(buscar)} de la lista de artemis")
    else:
        print("Porfavor digite una opcion que este en la lista de opciones")
    parar = str(input("Desea seguir digitando opciones?\nMarque 1 para si\nMarque 2 para no\n| "))
    if parar == "2":
        a = False
    