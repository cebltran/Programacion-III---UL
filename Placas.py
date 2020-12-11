import os


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def EsNumerico(entrada):
    if entrada in ['0','1','2','3','4','5','6','7','8','9']:
         Numero= True
    else:
         Numero = False
    return Numero

def Valida (Cadena):
    letras = 0
    EsNumero = False
    Mensaje =""
    for i, caracter in enumerate(Cadena):
        Caracter = Cadena[i]
        if EsNumerico(Caracter):
            Caracter = '.1'
            EsNumero = True

        if i == 0:
            if Caracter == '.1':
                iniciaconnumero = True
            else:
                iniciaconnumero = False
                letras = letras + 1
            Valor = PrimerCaracter.get(Caracter)

            if Valor is None:
                print ("\033[11;0H"+"\033[0;34;44m"+u"\u2588"*80+"\033[0m")
                print("El primer caracter no es valido")
                break

        if i == 1 and not Valor is None:
            if EsNumero == False:
                letras = letras + 1
            Valor = SegundoCaracter.get(Caracter)
            if Valor is None:
                print("\033[11;0H" + "\033[0;34;44m" + u"\u2588" * 80 + "\033[0m")
                print("El Segundo caracter no es valido")
                break

        if i == 2 and not Valor is None:
            if EsNumero == False:
                letras = letras + 1
            Valor = TercerCaracter.get(Caracter)
            if Valor is None:
                print("\033[11;0H" + "\033[0;34;44m" + u"\u2588" * 80 + "\033[0m")
                print("El Tercer caracter no es valido")
                break

        if i == 3 and not Valor is None:
            if EsNumero == False:
                letras = letras + 1
            Valor = CuartoCaracter.get(Caracter)
            if Valor is None:
                print("\033[11;0H" + "\033[0;34;44m" + u"\u2588" * 80 + "\033[0m")
                print("El Cuarto caracter no es valido")
                break
        if i > 3 and i< 7 :
            if  EsNumero ==  True:
                Valor = 'Valido'
            else:
                print("\033[11;0H" + "\033[0;34;44m" + u"\u2588" * 80 + "\033[0m")
                print("Revise la placa, la posicion " + str(i+1) + " debe ser numerica")
                break

    if Valor == 'Valido':
        if iniciaconnumero == False:
            LetrasaBuscar = Cadena[0:letras]
        elif iniciaconnumero == True and (Cadena[1] == 'T' or Cadena[1] == 'B'):
            LetrasaBuscar = "#" + Cadena[1]
        else:
            LetrasaBuscar = ".1"
        if Prefijo.get(LetrasaBuscar) is None:
            print("El patron no ha sido configurado")
        else:
            print(Prefijo.get(LetrasaBuscar))


Provincia ={
    '1': ' Bocas del Toro',
    '2': ' Coclé',
    '3': ' Colón',
    '4': ' Chiriquí',
    '5': ' Darién',
    '6': ' Herrera',
    '7': ' Los Santos',
    '8': ' Panamá',
    '9': ' Veraguas'
}

PrimerCaracter = {
    'C': ['Valido'],
    'R': ['Valido'],
    'M': ['Valido'],
    'A': ['Valido'],
    'P': ['Valido'],
    'H': ['Valido'],
    'D': ['Valido'],
    'E': ['Valido'],
    'G': ['Valido'],
    '.1': ['Valido']}

SegundoCaracter = {
    'A': ['Valido'],
    'B': ['Valido'],
    'C': ['Valido'],
    'D': ['Valido'],
    'E': ['Valido'],
    'F': ['Valido'],
    'G': ['Valido'],
    'H': ['Valido'],
    'I': ['Valido'],
    'J': ['Valido'],
    'K': ['Valido'],
    'L': ['Valido'],
    'M': ['Valido'],
    'N': ['Valido'],
    'O': ['Valido'],
    'P': ['Valido'],
    'Q': ['Valido'],
    'R': ['Valido'],
    'S': ['Valido'],
    'T': ['Valido'],
    'U': ['Valido'],
    'V': ['Valido'],
    'W': ['Valido'],
    'X': ['Valido'],
    'Y': ['Valido'],
    'Z': ['Valido'],
    '.1': ['Valido']}

TercerCaracter = {
    'D': ['Valido'],
    'M': ['Valido'],
    'I': ['Valido'],
    '.1': ['Valido']}

CuartoCaracter = {
    'M': ['Valido'],
    '.1': ['Valido']}


# Diccionario de prefijos
Prefijo = {
    'CP': ['Autoridad del Canal'],
    'CD': ['Placas Diplomaticas'],
    'CC': ['Curepo Consular'],
    'RCD': ['Placa diplomatica'],
    'MCD': ['Placa diplomatica'],
    'MADM': ['Placa diplomatica'],
    'ADM': ['Placa de administracion'],
    'PH': ['Placa diplomatica'],
    'PE': ['Placa diplomatica'],
    'MMI': ['Placa diplomatica'],
    'RMI': ['Placa diplomatica'],
    'PR': ['Periodista'],
    'HP': ['Radioaficionados'],
    'D': ['Demostracion'],
    'E': ['Fiscales y Jueces'],
    'G': ['Gobierno'],
    'MA': ['Motocicleta'],
    'MB': ['Metrobus'],
    'CH': ['Cuerpo Honorario'],
    'MI': ['Mision Internacional'],
    'AA': ['Automovil Particular'],
    'AB': ['Automovil Particular'],
    'AC': ['Automovil Particular'],
    'AD': ['Automovil Particular'],
    'AE': ['Automovil Particular'],
    'AF': ['Automovil Particular'],
    'AG': ['Automovil Particular'],
    'AH': ['Automovil Particular'],
    'AI': ['Automovil Particular'],
    'AJ': ['Automovil Particular'],
    'AK': ['Automovil Particular'],
    'AL': ['Automovil Particular'],
    'AM': ['Automovil Particular'],
    'AN': ['Automovil Particular'],
    'AO': ['Automovil Particular'],
    'AP': ['Automovil Particular'],
    'AQ': ['Automovil Particular'],
    'AR': ['Automovil Particular'],
    'AS': ['Automovil Particular'],
    'AT': ['Automovil Particular'],
    'AU': ['Automovil Particular'],
    'AV': ['Automovil Particular'],
    'AW': ['Automovil Particular'],
    'AX': ['Automovil Particular'],
    'AY': ['Automovil Particular'],
    'AZ': ['Automovil Particular'],
    '.1': ['Placa desactualizada o vehiculo operativo del estado'],
    '#T': ['Taxi'],
    '#B': ['Bus - Diablo rojo'],

}


PC = PrimerCaracter.keys()
salir = 1
while salir != 0:
    print("***************************************************")
    print("****************Cero (0) - Salir -*****************")
    Placa = input("Ingrese el numero de placa: ")
    Placa = Placa.upper()
    if len(Placa) != 6:
        if Placa == '0':
            break
        print("La longitud de la placa debe ser de 6 letras o numeros")
    else:
            Valida(Placa)

clear()



