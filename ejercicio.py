import random

print("-----------------------------------------")
print("----------PIEDRA-PAPEL-TIJERAS-----------")
print("-----------------------------------------")

print("1.Piedra")
print("2.Papel")
print("3.Tijera")

PC = random.randint(1,3)

# INPUT
player = int(input("Escoga su opción: "))

# PROCESS
if player == PC:
    print("Hubo un empate.") 

elif player == 1 and PC == 3:
    print("Ganaste, piedra le gana a tijera.")
elif player == 1 and PC == 2:
    print("Perdiste, La pc escogio papel entonces le gana a piedra.") 
elif player == 2 and PC == 1:
    print("Ganaste, papel le gana a piedra.") 
elif player == 2 and PC == 3:
    print("Perdiste, La pc escogio tijera entonces le gana a papel.") 
elif player == 3 and PC == 2:
    print("Ganaste, tijera le gana a papel.") 
elif player == 3 and PC == 1:
    print("Perdiste, La pc escogio piedra entonces le gana a tijera.") 

else:
    print("-----------------")
    print("Entrada inválida.") # OUTPUT
    print("-----------------") 


