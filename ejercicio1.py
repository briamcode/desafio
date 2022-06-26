# Este bloque de codigo permite obtener las primeras y las ultimas letras que componen una palabra

wellcome = """

Bienvenido a solucion del ejercicio # 1

"""
print(wellcome)

# Iteramos en la palabra ingresada y agregamos cada letra a una lista
def wordCount():
    list1 = []

    for i in word:
        list1.append(i)
            
    print("Las dos primeras letras de tu palabra son : ", list1[0], list1[1])  
    print("Las tres primeras letras de tu palabra son : ",list1[0], list1[1], list1[2])
    print("Las ultimas dos letras de tu palabra son : ", list1[-2], list1[-1])
    print("La ultima letra de tu palabra es : ", list1[-1])

# Pedimos al usuario digitar una sola palabra sin espacios mediante un bucle while      
word = input('Digita una palabra : ')
while " " in word:
    print("")
    print("Digita una sola plabra sin espacios ")
    word = input('Digita una palabra : ')
print("")
wordCount()        

    

