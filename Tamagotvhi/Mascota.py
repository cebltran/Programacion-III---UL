import os
class Turno:
    Genero = 'Macho'
    def __init__(self, limite):
        self.alimentar = limite - 1
        self.jugar = limite - 1
Hambre = 10
Felicidad = 10
Salud = 0
salir = 1
c = '.°.'
Nombre = input("Cual es el nombre de su Mascota?:")
Animal = input("Que animal es su tamagotchi?:")

while salir != 0:
    print(Nombre + " necesita cuidados, recuerda que es un " + Animal + ' ' + Turno.Genero)
    Clave = int(input("Elija una Opción: 1) Alimentar 2) Jugar 3)Abandonar Mascota:  "))
    if Clave == 1:
        Hambre = Hambre + 2
        if Hambre > 10:
            Salud = Salud + 2
            Hambre = 10
    elif Clave == 2:
        Felicidad = Felicidad + 3
        if Felicidad > 10:
            Felicidad = 10
    elif Clave == 3:
        print("Su mascota ha sido abandonada")
        salir = 0

    if salir != 0:
        Pasada = Turno(Hambre)
        Hambre = Pasada.alimentar
        Pasada = Turno(Felicidad)
        Felicidad = Pasada.jugar
        if Hambre <= 0:
            print("Su mascota murio de hambre")
            salir = 0
        elif Salud > 10:
            print("Su mascota enfermo y murio")
            salir = 0

    print(str(Hambre) +     " - Alimentado - " + str(c * Hambre))
    print(str(Felicidad) +  " - Bienestar  - " + str(c * Felicidad))
    print(str(Salud) +      " - Salud      - " + str(c * Salud))
    os.system("cls")