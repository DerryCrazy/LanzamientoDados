import random #librerias

def tirar_dado(): #funcion 
    return random.randint(1, 6) #numeros del 1 al 6 randoms

def principal(): #funcion principal
    print("¡Hola! Esto es un simulador de dados.") #mensaje
    resultados = {total: 0 for total in range(2, 13)} #nO SE PUEDE obtener 1 o 0
    while True:#ciclo
        lanzar = input("¿Te gustaría tirar los dados? (s/n): ").lower() #capturar opcion s para si y n no
        if lanzar == 'n': #si es no se para el programa
            break

        dado1 = tirar_dado()    
        dado2 = tirar_dado()    
        total = dado1 + dado2   
        resultados[total] += 1  

        print(f"Obtuviste: {dado1} + {dado2} = {total}") #mostrar mensaje

    print("\nResumen de tiradas:")
    for total, veces in resultados.items():
        print(f"Total {total}: {veces} veces")

if __name__ == "__main__":
    principal()
