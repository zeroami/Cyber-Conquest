import os
import sys
import time

# Colores para la terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}")
    print("  ██████╗██╗   ██╗██████╗ ███████╗██████╗ ")
    print(" ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗")
    print(" ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝")
    print(" ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗")
    print(" ╚██████╗   ██║   ██████╔╝███████╗██║  ██║")
    print("  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝")
    print("          CONQUEST: CYBER SECURITY GAME   ")
    print(f"            [ 2025 Edition - v1.2 ]       {bcolors.ENDC}\n")

def main_menu():
    clear_screen()
    banner()
    print(f"{bcolors.HEADER}--- SELECCIONA TU MISIÓN ---{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}1.{bcolors.ENDC} Mundo 1: Bastión y Protocolo (Defensa de Red)")
    print(f"{bcolors.OKGREEN}2.{bcolors.ENDC} Mundo 2: Carnaval de Sombras (Ingeniería Social)")
    print(f"{bcolors.OKGREEN}3.{bcolors.ENDC} Mundo 3: Ciudad Fantasma (Hacking Web - Bloqueado)")
    print(f"{bcolors.OKGREEN}4.{bcolors.ENDC} Ver Aviso Legal (SECURITY.md)")
    print(f"{bcolors.WARNING}0. Salir{bcolors.ENDC}")
    
    choice = input(f"\n{bcolors.BOLD}root@conquest:~# {bcolors.ENDC}")
    return choice

def play_world_1():
    clear_screen()
    banner()
    print(f"{bcolors.OKBLUE}[MUNDO 1: BASTIÓN Y PROTOCOLO]{bcolors.ENDC}")
    print("Cargando módulos de defensa de red...")
    time.sleep(1)
    print(f"\n{bcolors.OKCYAN}OPCIONES:{bcolors.ENDC}")
    print("a) Leer Manual de Defensa (Markdown)")
    print("b) Lanzar Script de Honeyport (Trampa)")
    print("c) Volver al menú")
    
    sub_choice = input(f"\n{bcolors.BOLD}root@world1:~# {bcolors.ENDC}")
    
    if sub_choice == 'a':
        os.system('cat 01-Bastion-Protocolo/Manual_Defensa.md | more')
    elif sub_choice == 'b':
        print(f"{bcolors.FAIL}[!] Iniciando Honeyport... (Requiere permisos sudo){bcolors.ENDC}")
        # Aquí lanzaría tu script .sh si existe en la carpeta
        os.system('sudo bash 01-Bastion-Protocolo/honeyport.sh')
    
def play_world_2():
    clear_screen()
    banner()
    print(f"{bcolors.HEADER}[MUNDO 2: CARNAVAL DE SOMBRAS]{bcolors.ENDC}")
    print("Accediendo a la base de datos de psicología conductual...")
    time.sleep(1)
    os.system('cat 02-Carnaval-Sombras/Guia_Ingenieria_Social.md | more')

def show_security():
    clear_screen()
    banner()
    os.system('cat SECURITY.md | head -n 40') # Muestra el principio de los idiomas
    input(f"\n{bcolors.BOLD}Presiona Enter para continuar...{bcolors.ENDC}")

if __name__ == "__main__":
    while True:
        option = main_menu()
        if option == '1':
            play_world_1()
        elif option == '2':
            play_world_2()
        elif option == '3':
            print(f"{bcolors.FAIL}\n[!] ERROR: Acceso denegado. Completa los mundos anteriores.{bcolors.ENDC}")
            time.sleep(2)
        elif option == '4':
            show_security()
        elif option == '0':
            print(f"{bcolors.OKBLUE}Saliendo del sistema... Adiós, Hacker.{bcolors.ENDC}")
            break
        else:
            print(f"{bcolors.FAIL}Comando no reconocido.{bcolors.ENDC}")
            time.sleep(1)
