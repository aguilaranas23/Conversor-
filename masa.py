#autor:constanza contreras,anastasia aguilar
#fecha:02/11/23
#descripcion: este modulosirve para la conversion de unidades


def kilogramos_gramos (masa):
    return masa *1000

if __name__== "__main___":

    kilogramos= float(input("ingrese los kilogramos a convertir \n"))
    print(kilogramos_gramos(kilogramos))