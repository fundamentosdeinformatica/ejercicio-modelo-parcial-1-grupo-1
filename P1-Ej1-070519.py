# Una empresa de ómnibus de larga distancia quiere renovar los vehiculos con
# más de 10 años de antigüedad. Desarrollar un programa donde primero se ingrese
# el año en curso, luego se ingrese el año de fabricación de los vehículos hasta
# ingresar un año en cero. El año de fabricación no puede ser menor a 1990, ni
# mayor al año en curso. Se pide informar:
# a) Cuantos vehículos se deben renovar.
# b) Cuantos vehículos tienen 10 años exactos.
# c) El porcentaje de vehiculos a renovar.
# d) El ómnibus más viejo que tiene la empresa.

def IngresarAnioFabricacion(anioActual):
    anio = int(input("Ingrese año de fabricacion: "))
    while (anio != 0 and (anio < 1990 or anio > anioActual)):
        print("El año ingresado es incorrecto.")
        anio = int(input("Ingrese año de fabricacion: "))
    return anio


exacto10 = 0 # Omnibus de 10 años
renovar = 0 # Omnibus a renovar
total = 0 # Total de omnibus

anioActual = int(input("Ingrese año en curso: "))
# Si el año de fabricacion no puede ser menor a 1990, el año actual tampoco.
while (anioActual < 1990):
    print("El año actual no puede ser menor a 1990")
    anioActual = int(input("Ingrese año en curso: "))

anio = IngresarAnioFabricacion(anioActual)
masViejo = anio # El primero que se ingresa es el más viejo ingresado hasta el momento.

while (anio != 0):
    total = total + 1
    
    if (anioActual - anio == 10):
        exacto10 = exacto10 + 1
    elif (anioActual - anio > 10):
        renovar = renovar + 1
        
    if (masViejo > anio):
        masViejo = anio
    
    anio = IngresarAnioFabricacion(anioActual)

if (total == 0):
    print("No se ingreso ningun año de fabricacion.")
else:
    print("Se deben renovar", renovar, "vehículos.")
    print("Hay", exacto10, "vehículos con exactamente 10 años.")
    print("El porcentaje de vehículos a renovar es:", renovar*100/total, "%")
    print("El ómnibus más viejo fue fabricado en el año", masViejo)
