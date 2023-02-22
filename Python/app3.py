finalistas = 3
lista_nombres = []
lista_marcas = []
for i in range (0,finalistas):
    lista_nombres.append(str(input(f"Ingrese el nombre del finalista {i+1} : ")))
    lista_marcas.append(float(input(f"Ingrese la marca de salto del finalista {i+1} en metros: ")))
mayor_marca = max(lista_marcas)
posicion = lista_marcas.index(mayor_marca)
if mayor_marca > 15.5:
    record = f"!El/La finalista {lista_nombres[posicion]} rompió el record de 15,5 metros con una marca de {lista_marcas[posicion]} metros por lo cual se le realizará un pago de 500 millones!"
    print(f"El/La finalista ganador de la medalla de oro es {lista_nombres[posicion]},\n{record}")
else:
    print(f"El/La finalista ganador de la medalla de oro es {lista_nombres[posicion]} con una marca de {mayor_marca} metros")
