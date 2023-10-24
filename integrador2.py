from readchar import readkey, key


while True:
    print(" escoge una tecla: ")
    tecla = readkey()
    if tecla == key.UP:
        print(f"felicidades escogiste la tecla correcta ↑ UP!")
        break
    else:
        print(f"has oprimido una de las tecla "{caracter}", intentalo de nuevo")
