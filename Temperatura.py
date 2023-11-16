#Autor:constanza contreras,anstasia agular
#Fecha:02/11/2023
#Descripcion: Este Modulo permite la conversíón de unidades.

def celsius_fahrenheit(grados):
    return (grados * 9/5) + 32

if __name__=="__main__":

    celsius= float(input("Ingrese los grados a convertir \n"))
    print(celsius_fahrenheit(celsius))