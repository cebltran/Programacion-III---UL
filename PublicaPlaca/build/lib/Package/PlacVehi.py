"""
Universidad Latina de Panama
Programación III
DOcente: Abdiel Gadiel Martinez
Autor: César Beltran
Diciembre 2020
"""
import os
sMensaje=""

def clear():
    """
    Funcion para limpiar la consola segun sistema operativo
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
#Funcion para determinar si un caracter es numerico
def EsNumerico(entrada):
    """
    :Retorna falso / verdadero
    """
    if entrada in ['0','1','2','3','4','5','6','7','8','9']:
         Numero= True
    else:
         Numero = False
    return Numero
#Funcion para Validar la placa
def Valida (Cadena):
    """

    :param Cadena: Placa ingresada por el usuario
    :return: Tipo de vehiculo
    """
    letras = 0
    """
    :letras: Esta variuable lleva la cuenta de cuan tas letras tiene la placa
    """
    EsNumero = False
    Mensaje =""
    """
    :EsNumero: Inicializacion de la variable para determinar si un caracter es numerico
    :Mensaje: Inicializacion de la variable que retornara el mensaje   
    """
    for i, caracter in enumerate(Cadena):
        Caracter = Cadena[i]
        """
        :i : Recorre toda la cadena escrita en el programa
        :Caracter: Contiene el caracter de la cadena en la posicion i
        """
        if EsNumerico(Caracter):
            """
            Si el carcter es numerico busca en las listas con una constante .1,
            si lo encuentra en el diccionario el numero es valido enl a posicion
            """
            Caracter = '.1'
            EsNumero = True

        if i == 0:
            """
            Si el primer caracter i==0 es numerico le indica al programa que inicia por numero la cadena, de lo contrario
            inicia el conteo de letras
            """
            if Caracter == '.1':
                iniciaconnumero = True
            else:
                iniciaconnumero = False
                letras = letras + 1
            Valor = PrimerCaracter.get(Caracter)
            """
            Busca el caracter en un diccionario diseñado con las PRIMERAS letras validas para las placas investigadas.
            Cuando el caracter no es encontrado en la  posicion Retorna una linea celeste e informa que el 
            caracter no es valido 
            """

            if Valor is None:
                print ("\033[11;0H"+"\033[0;34;44m"+u"\u2588"*80+"\033[0m")
                print("El primer caracter no es valido")
                break

        if i == 1 and not Valor is None:
            """
            Entra si el primer caracter es valido.
            Si el segundo caracter i==1 No es numerico incrementa el conteo de las letras
            """
            if EsNumero == False:
                letras = letras + 1
            Valor = SegundoCaracter.get(Caracter)
            """
            Busca el caracter en un diccionario diseñado con las SEGUNDAS letras validas para las placas investigadas.
            Cuando el caracter no es encontrado en la  posicion Retorna una linea celeste e informa que el 
            caracter no es valido 
            """

            if Valor is None:
                print("\033[11;0H" + "\033[0;34;44m" + u"\u2588" * 80 + "\033[0m")
                print("El Segundo caracter no es valido")
                break

        if i == 2 and not Valor is None:
            """
            Entra si el segundo  caracter es valido.
            Si el TERCER caracter i==2 No es numerico incrementa el conteo de las letras
            """
            if EsNumero == False:
                letras = letras + 1
            Valor = TercerCaracter.get(Caracter)
            """
            Busca el caracter en un diccionario diseñado con las TERCERAS letras validas para las placas investigadas.
            Cuando el caracter no es encontrado en la  posicion Retorna una linea celeste e informa que el 
            caracter no es valido 
            """

            if Valor is None:
                print("\033[11;0H" + "\033[0;34;44m" + u"\u2588" * 80 + "\033[0m")
                print("El Tercer caracter no es valido")
                break

        if i == 3 and not Valor is None:
            """
            Entra si el tercer caracter es valido.
            Si el CUARTO caracter i==3 No es numerico incrementa el conteo de las letras
            """

            if EsNumero == False:
                letras = letras + 1
            Valor = CuartoCaracter.get(Caracter)
            """
            Busca el caracter en un diccionario diseñado con las CUARTAS letras validas para las placas investigadas.
            Cuando el caracter no es encontrado en la  posicion Retorna una linea celeste e informa que el 
            caracter no es valido 
            """

            if Valor is None:
                print("\033[11;0H" + "\033[0;34;44m" + u"\u2588" * 80 + "\033[0m")
                print("El Cuarto caracter no es valido")
                break

        if i > 3 and i< 7 :
            """
            Las placas deben ser numericas de la posicion 4 a la 6.
            Valida si el valir es numerico en esta posicion e inmediatamente lo trata como valido
            de otra forma retorna una linea celeste reportando el error  
            """
            if  EsNumero ==  True:
                Valor = 'Valido'
            else:
                print("\033[11;0H" + "\033[0;34;44m" + u"\u2588" * 80 + "\033[0m")
                print("Revise la placa, la posicion " + str(i+1) + " debe ser numerica")
                break
    """
    Al terminar de recorrer la cadena y tenemos un valor Valido en la busqueda ya sabemos que todos los caracteres
    estan ubicados en la posicion correcta y procedemos a buscar en la lista correspondiente
    """

    if Valor == 'Valido':
        if iniciaconnumero == False:
            """
            Si la cadena inicia con letras
            :LetrasaBuscar : Determina la cadena a buscar en el diccionario de placas por tipo
            :letras: cantidad de letras a buscar
            """
            LetrasaBuscar = Cadena[0:letras]
        elif iniciaconnumero == True and (Cadena[1] == 'T' or Cadena[1] == 'B'):
            """
            Inicia con numero pero la segunda posicion es T o B
            :LetrasaBuscar : Determina la cadena a buscar en el diccionario de placas por tipo
            :letras: cantidad de letras a buscar
            En el diccionario se configuro este tipo de placa comenzando en el simbolo #
            """
            LetrasaBuscar = "#" + Cadena[1]
        else:
            """
            Sin inicia por numero busca .1 definido en el diccinario para placas numericas
            """
            LetrasaBuscar = ".1"
        """
        Se ejecuta la busqueda en el diccionario principal el patron depurado
        """
        if Prefijo.get(LetrasaBuscar) is None:
            print("El patron no ha sido configurado")
        else:
            print(Prefijo.get(LetrasaBuscar))

#PrimerCaracter: Diccionario que contiene los caracteres validos para la primera posicion
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
    'T': ['Valido'],
    '.1': ['Valido']}
#SegundoCaracter: Diccionario que contiene los caracteres validos para la segunda posicion

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

#TercerCaracter: Diccionario que contiene los caracteres validos para la Tercera posicion


TercerCaracter = {
    'D': ['Valido'],
    'M': ['Valido'],
    'I': ['Valido'],
    '.1': ['Valido']}

#CuartoCaracter: Diccionario que contiene los caracteres validos para la cuarta posicion


CuartoCaracter = {
    'M': ['Valido'],
    '.1': ['Valido']}


#Prefijo: Diccionario que contiene las placas validas

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
    'T': ['Taxi'],
    '#T': ['Taxi'],
    '#B': ['Bus - Diablo rojo'],

}




