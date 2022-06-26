# Este bloque de codigo permite totalizar una cuenta de restaurante y dividir el valor entre un numero de personas
wellcome = """

Bienvenido a solucion del ejercicio # 2

"""
print(wellcome)

def data():
    try:
        # Usamos casting para evitar que el usuaruio digite valores que no son numericos 
        bill = int(input('Digita el valor de la cuenta : '))
        people = int(input('Digita el numero de personas que pagaran la cuenta : '))
        tip = int(input('Digita el porcetaje de propina : '))
        taxes = int(input('Digita el porcentaje de impuestos : '))

        print("")
        # Realizamos las operaciones aritmeticas para obtener los valores finales
        percentageTip = bill * (tip / 100)
        subTotal = bill + percentageTip
        percentageTaxes = subTotal * (taxes / 100)
        total = subTotal + percentageTaxes
        paymentPerPerson = total / people
        print("")
        print("El valor de la cuenta es :    ", bill)
        print("El valor de la propina es :    ", percentageTip)
        print("El valor de los impuestos es : ", percentageTaxes)
        print("El total de la cuenta es :    ", total)
        print("")
        print("A cada persona le corresponde pagar", paymentPerPerson)
        print("")

    except ValueError:
        print("")
        print("Digita solo numeros")
        print("")
        # Volvemos a llamar la funcion data para que el script no se cierre tras un error de digitacion
        data()

data()