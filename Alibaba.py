CntIntentos=10
FraseClave= "Ábrete Sésamo"
Intento = 1
NombreLadron =input("Dame tu nombre: ")
while Intento <= CntIntentos:
    Clave = input(NombreLadron + ",dime la clave para abrir la Cueva: ")
    if Clave == FraseClave:
        print("FELICIDADES!!!" + NombreLadron + " ha accedido a los secretos de la cueva!!!")
        Intento = 10
    else:
        if (CntIntentos - Intento) == 0:
            print("LA CUEVA SE HA CERRADO PERMANENTEMENTE, LO LAMENTAMOS " + NombreLadron)
        else:
            print("*****Cuida la ortografía****")
            print(NombreLadron, "denegado el acceso a los tesoros y solo tiene " + str(CntIntentos - Intento) + " intentos antes de cerrar por siempre la cueva")
    Intento += 1




