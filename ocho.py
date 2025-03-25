
# todo: Resolución

diccionario = {"andres": 19, "critobal": 55, "melanie": 15}

for nombre, edad in diccionario.items():
    print("la edad de ", nombre, "es:", edad)
    
nuevo_nombre = input("¿cuál es su nombre?")
nueva_edad = input("¿cuál es su edad?")

diccionario[nuevo_nombre] = nueva_edad #actualiza el diccionario

for nombre, edad in diccionario.items():
    print("la edad de ", nombre, "es:", edad)
