import os
def menu():
    print("""
Bievenido al conversor de unidades de tiempo.
++++++++++++++++++++++++++++++++++++++++++++++
1) Segundos a Minutos
2) Segundos a Horas
3) Minutos a Segundos
4) Minutos a Horas
0)Salir
    """)
def segundos_a_minutos():
    segundos=int(input("Ingrese la cantidad de segundos: "))
    min=segundos//60
    seg=segundos%60
    print(f"{segundos} segundos equivale a {min} minutos {seg} segundos.")
def segundos_a_horas():
    segundos=int(input("Ingrese la cantidad de segundos: "))
    min=segundos//60
    hor=min//60
    min=min%60
    seg=segundos%60
    print(f"{segundos} segundos equivale a {hor} horas {min} minutos {seg} segundos.")
def minutos_a_segundos():
    minutos=int(input("Ingrese la cantidad de minutos: "))
    segundos=int(input("Ingrese la cantidad de segundos: "))
    seg=(minutos*60)+segundos
    print(f"{minutos} minutos y {segundos} segundos equivale a {seg} segundos.")
def minutos_a_horas():
    minutos=int(input("Ingrese la cantidad de minutos: "))
    segundos=int(input("Ingrese la cantidad de segundos: "))
    hor=minutos//60
    min=minutos%60
    print(f"{minutos} minutos y {segundos} segundos equivale a {hor} horas {min} minutos {segundos} segundos.")
def main():
    continuar=True
    while continuar==True:
        menu()
        opcion=int(input("Seleccione una opcion: "))
        os.system("cls")
        if opcion==1:
            segundos_a_minutos()
        elif opcion==2:
            segundos_a_horas()
        elif opcion==3:
            minutos_a_segundos()
        elif opcion==4:
            minutos_a_horas()
        elif opcion==0:
            continuar=False
        else:
            print("Opcion incorrecta, intente nuevamente!")
        os.system("pause")
        os.system("cls")
    else:
        print("Gracias por utilizar mi programa!")
if __name__=="__main__":
    main()
#Falta hacer validacion de numeros negativos!!
