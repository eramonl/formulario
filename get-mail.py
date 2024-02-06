#!/usr/bin/python3
import sys
def main():
    argumentos = sys.argv
    nombre_script=argumentos[0]
    if len(argumentos) <= 1:
        print("No has puesto argumentos")
    else:
        buscar = str(argumentos[1]) 
        if buscar in lista:
            print(lista[buscar])
        else:
            print("No esta")

lista = {
"Mercedes":"mcast386@xtec.cat",
"Rayane":"rayane@rayane.sa",
"Mohamed":"moha@gmail.com",
"Jad":"jad@gmail.com",
"Oriol":"joam@gmail.com",
"Elias":"hola123@gmail.com",
"Armau":"arnau@gmail.com",
"Asdrúbal":"asdrubal@gmail.com",
"Adrian":"pedrosanchez@asix2.com",
"Eric":"eric@gmail.com",
"Emma":"pacosanz@gmail.com",
"nishwan":"nishwan@gmail.com",
"Javi":"javi@gmail.com",
"Novel":"novelferreras49@gmail.com",
"Bruno":"elcigala@gmail.com",
"David":"argentino@gmail.com",
"Judit":"judit@gmail.com",
"Joao":"joao@gmail.com",
"Laura":"laura@gmail.com",
"enrico":"123@gmail.com",
"Joel":"joelcobre@gmail.com",
"Aaron":"aaron@gmail.com",
"Moad":"moad@gmail.com"
}


main()