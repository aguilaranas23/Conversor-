#Autor:constanza contreras,anastasia aguilar
#Fecha:02/11/2023
#Descripcion: Este Modulo es el menu de conversion de unidades

import Temperatura as temp

def main():
    while True:
        opcion = input("Bienvenido, que unidades desea convertir?: \n" 
                "0. Salir del programa\n"
                "1. Celsius a Farenheit\n"
                "2. Kilogramos a gramos\n")
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                celsius= float(input("Ingrese los grados a convertir \n"))
                print(temp.celsius_fahrenheit(celsius))
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

main()