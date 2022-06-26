# Este bloque de codigo permite tomar tu edad actual para saber que edad tenias al año anterior y que edad tendras el proximo año

wellcome = """

Bienvenido a solucion del ejercicio # 3

"""
print(wellcome)

def ages():
    # Usamos try except para evitar que el usuario digite datos erroneos en la variable age
    try:
        name = input('Digita tu nombre : ')
        age = int(input('Digita tu edad : ')) 
        lastYear = age - 1 
        nextYear = age + 1
        print("")
        print(name, " El año pasado tenias ",lastYear, " años")
        print(name, " El proximo año tendras ",nextYear, " años")

    except ValueError:
        print("")
        print("Digita tu edad en numeros")
        print("")
        ages()


ages()