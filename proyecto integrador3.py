
import os
from readchar import readkey

#hacemos la funcion de limpiar la terminal
def limpiar_terminal():
    os.system('cls' if os.name=='nt' else 'clear')


print("oprime la letra n para comenzar un conteo, la meta es llegar a 50")

#creamos una variable que va aumentar cada vez  que se presione la n
contador=0

#realizamos el bucle
while True:
    tecla = readkey()

    if tecla == 'n':
        contador += 1
        limpiar_terminal()
        print(f" has oprimido '{tecla}' {contador} veces, sigue intentano pronto lo lograras")

        if contador == 50:
            limpiar_terminal()
            print(f"Felicitaciones, has presionado exitosamente la tecla 'n' {contador} veces")
            break

    else:
        print(f"Has presionado la tecla {tecla} en lugar de 'n', intentalo de nuevo")
