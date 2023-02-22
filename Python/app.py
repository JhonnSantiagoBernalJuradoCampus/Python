print("1.Qué operadores utiliza python en los siguientes casos\nA.División modular\nB.Exponenciación\nC.División que retorne entero.\nSolución:\n\tA.División modular: %\n\tB.Exponenciación: **\n\tC.División entero: //")
print("2. En la jerarquía de operadores, cuáles son los que más prioridad tienen cuando el intérprete de Python los evalúa?\nSOlución:\n\tPython prioriza los parentecis(()) y resuelve lo que hay adentro, después prioriza la exponenciación (**) luego la multiplicación (*) luego la división (/) luego la suma y la resta (+,-) ")
print("3. Si hay operadores de igual precedencia, en qué orden se ejecutan?\nA. De izquierda a derecha\nB. De derecha a izquierda\n\tA. De izquierda a derecha")
print("4. Que son las expresiones regulares en Python?\nSolución:\n\t Ejemplo: \tArea= base * altura\n• Intérprete evalúa expresión lado derecho\n• Resultado se asigna a dirección memoria.\n• Se almacena dirección memoria en variable lado izquierda.")
print("5. Enumere 5 tipos de datos en Python y suministre un valor deejemplo de cada uno.\nSolución:\n\t1. Tabla: [15,80,30]\n\t2. Tupla: {'Hola','Nombre',4}\n\t3. Boleano: True, False\n\t4. str: 'Hellow World'\n\t5. float: 15.2312323")
print("6. En sus propias palabras, qué son las funciones preconstruidas y proporcione 2 ejemplos.\nSolución:\n\tLas funciones preconstruidas vienen siendo un valor que al aplicarlo realiza una cierta acción ya predefinda:\n\tEjemplos:\n\t\tlen(x)\tLo que hace esta función preconstruida es dar el numero de datos que tenga una variable.\n\t\tmax(12,40,32)\tLo que hace es dar el numero maximo de los numero que estan dentro del ()")
print("7. Cuál es la diferencia entre un condicional simple y un condicional compuesto?\nSolución:\n\tLa diferencia entre un condicional simple y un condicional compuesto es que en el condicional simpre solo se pide que realice una acción si una sola situación se cumple, en cambio en el condicional compuesto hay distintas acciones que se pueden realizar dependiendo de los condicionales que se cumplan")
print("8. Escriba un bloque cualquiera de código en Python en donde utilice 2 condicionales (if) anidados.\nSolución:\n\t")
numero = 234
if numero % 2 ==0:
    if numero > 100:
        print("El numero es par y es mayor a 100")
    else:
        print("El numero es par y es menor que 100")
else:
    print("El numero es impar")
print("9. Construya un algoritmo en Python, que permita ingresar la información de un empleado e imprima el nombre, los apellidos y la antigüedad. Los datos que se deben solicitar son los siguientes:\n\t*Nombre \t*Teléfono \t*Año de ingreso a la empresa \t*Apellidos \t*Edad.\n")
nombre = str(input("Ingrese su Nombre:\n"))
telefono = input("Ingrese su numero de teléfono:\n")
año_ingreso = int(input("Ingrese el año en el que ingresó a la empresa:\n"))
apellidos = input("Ingrese sus apellidos:\n")
edad = input("Ingrese su edad:\n")
antiguedad = 2023-año_ingreso
print(f"Su nombre es {nombre} sus apellidos son " f"{apellidos} y lleva " f"{antiguedad} años en la empresa")
print("10. En su casa le solicitan que realice un algoritmo en Python, que permita calcular el valor a pagar por concepto de energía eléctrica. Los datos que se conocen son los siguientes:\n-Mes de consumo\n-Valor kw\n-Total kw consumido en el mes \n-estrato")
mes_consumo = "Enero"
valor_kw = 200
total_kw = 6000
estrato = 2
pago = valor_kw*total_kw*estrato
print(f"El valor total a pagar el mes de {mes_consumo} es ${pago}")