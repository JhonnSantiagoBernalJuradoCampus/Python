sueldo_km = float(input("Ingrese el sueldo básico por kilometro recorrido: "))
numero_total_km = float(input("Ingrese el numero de kilometros recorridos durante toda la vuelta: "))
lider = float(input("Ingrese el numero de kilometros recorridos con la camiseta líder: "))
if numero_total_km < 3277:
    if lider > 1800:
        numero_km = numero_total_km+(lider*0.25)
        total = sueldo_km * numero_km
    else:
        total = sueldo_km * numero_total_km
    print(f"El valor total a pagar es de ${total}")
else:
    print("Es imposible que haya recorrido mas de 3277km en la vuelta")