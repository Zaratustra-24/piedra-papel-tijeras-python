Nombre1= input("¿Cómo se llamará el jugadpr 1? ") 
Nombre2= input("¿Cómo se llamará el jugadpr 2? ") 


jugador1= input("¡Hola jugador1! ¿Qué eliges? ¿Piedra, papael o tijeras?: ").lower()
jugador2= input("¡Hola jugador2! ¿Qué eliges? ¿Piedra, papael o tijeras?: ").lower()


condicion1=(jugador1 == "piedra" and jugador2 == "tijeras")
condicion2=(jugador1 == "papel" and jugador2 == "piedra")
condicion3=(jugador1 == "tijeras" and jugador2 == "papel")

if jugador1 == jugador2:
    print("¡Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado", Nombre1)
else:
    print("Ha ganado", Nombre2)
print(jugador1)