import os
import sys
import time
import json
from datetime import datetime

PROGRESS_FILE = "progress.json"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
    print("          CONQUEST: CYBER SECURITY GAME by github.com/zeroami  ")
    print(f"            [ 2026 Edition - v2.0 ]       {bcolors.ENDC}\n")

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"completed": [], "started": [], "last_access": None}

def save_progress(progress):
    progress["last_access"] = datetime.now().isoformat()
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)

def mark_world_started(world_id, progress):
    if world_id not in progress["started"]:
        progress["started"].append(world_id)
        save_progress(progress)

def mark_world_completed(world_id, progress):
    if world_id not in progress["completed"]:
        progress["completed"].append(world_id)
        save_progress(progress)

def show_progress(progress):
    total = 8
    completed = len(progress["completed"])
    started = len(progress["started"]) - completed

    print(f"\n{bcolors.HEADER}--- PROGRESO DEL JUGADOR ---{bcolors.ENDC}")
    print(f"Mundos completados: {completed}/{total}")
    print(f"Mundos en progreso: {started}")

    if completed > 0:
        pct = (completed / total) * 100
        bar_len = 30
        filled = int(bar_len * completed // total)
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"\n[{bar}] {pct:.0f}%")

    if progress["completed"]:
        print(f"\n{bcolors.OKGREEN}Completados:{bcolors.ENDC}")
        for w in progress["completed"]:
            print(f"  ✓ {w}")

    if progress.get("last_access"):
        print(f"\nUltimo acceso: {progress['last_access'][:19]}")

def read_markdown(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"\n{content}")
    else:
        print(f"{bcolors.FAIL}[!] Archivo no encontrado: {filepath}{bcolors.ENDC}")

def main_menu():
    clear_screen()
    banner()
    progress = load_progress()
    show_progress(progress)

    print(f"\n{bcolors.HEADER}--- SELECCIONA TU MISION ---{bcolors.ENDC}")
    print(f"\n{bcolors.OKGREEN}╔══ FASE 1: FUNDAMENTOS Y DEFENNA ══╗{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}1.{bcolors.ENDC} Mundo 1: Bastion y Protocolo (Defensa de Red)")
    print(f"{bcolors.OKGREEN}2.{bcolors.ENDC} Mundo 2: Carnaval de Sombras (Ingenieria Social)")
    print(f"{bcolors.OKGREEN}3.{bcolors.ENDC} Mundo 3: Laberinto Web (Hacking Web)")
    print(f"\n{bcolors.FAIL}╔══ FASE 2: OFENSIVA (RED TEAM) ══╗{bcolors.ENDC}")
    print(f"{bcolors.FAIL}4.{bcolors.ENDC} Mundo 4: Laboratorio Binario (Malware)")
    print(f"{bcolors.FAIL}5.{bcolors.ENDC} Mundo 5: Taller de Exploits (Buffer Overflow)")
    print(f"{bcolors.FAIL}6.{bcolors.ENDC} Mundo 6: Mar de Frecuencias (WiFi & Radio)")
    print(f"\n{bcolors.OKBLUE}╔══ FASE 3: ESTRATEGIA Y LEGALIDAD ══╗{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}7.{bcolors.ENDC} Mundo 7: Camara del Enigma (Criptografia)")
    print(f"{bcolors.OKBLUE}8.{bcolors.ENDC} Mundo 8: Gobernanza (Leyes y Etica)")
    print(f"\n{bcolors.WARNING}0. Salir{bcolors.ENDC}")

    choice = input(f"\n{bcolors.BOLD}root@conquest:~# {bcolors.ENDC}")
    return choice

def world_menu(world_num, world_name, options):
    clear_screen()
    banner()
    print(f"{bcolors.OKCYAN}[MUNDO {world_num}: {world_name}]{bcolors.ENDC}")
    print(f"{bcolors.HEADER}{'=' * 40}{bcolors.ENDC}\n")

    for i, (label, _) in enumerate(options, 1):
        print(f"{bcolors.OKGREEN}{i}.{bcolors.ENDC} {label}")
    print(f"{bcolors.WARNING}0.{bcolors.ENDC} Volver al menu principal")

    choice = input(f"\n{bcolors.BOLD}root@world{world_num}:~# {bcolors.ENDC}")
    return choice

def play_world_1():
    progress = load_progress()
    mark_world_started("Mundo 1", progress)

    options = [
        ("Leer Manual de Defensa", lambda: read_markdown("01-Bastion-Protocolo/Manual_Defensa.md")),
        ("Laboratorio: Honeyport", lambda: run_lab("01-Bastion-Protocolo/lab_honeyport.py")),
        ("Script: Honeyport (bash)", lambda: os.system("sudo bash 01-Bastion-Protocolo/honeyport.sh 2>/dev/null || echo '[!] Script no disponible'")),
        ("Marcar como completado", lambda: mark_world_completed("Mundo 1", progress)),
    ]

    while True:
        choice = world_menu(1, "BASTION Y PROTOCOLO", options)
        if choice == '0':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            options[int(choice) - 1][1]()
            input(f"\n{bcolors.BOLD}Presiona Enter para continuar...{bcolors.ENDC}")

def play_world_2():
    progress = load_progress()
    mark_world_started("Mundo 2", progress)

    options = [
        ("Leer Guia de Ingenieria Social", lambda: read_markdown("02-Carnaval-Sombras/Guia_Ingenieria_Social.md")),
        ("Quiz: OSINT", lambda: run_lab("02-Carnaval-Sombras/quiz_osint.py")),
        ("Marcar como completado", lambda: mark_world_completed("Mundo 2", progress)),
    ]

    while True:
        choice = world_menu(2, "CARNAVAL DE SOMBRAS", options)
        if choice == '0':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            options[int(choice) - 1][1]()
            input(f"\n{bcolors.BOLD}Presiona Enter para continuar...{bcolors.ENDC}")

def play_world_3():
    progress = load_progress()
    mark_world_started("Mundo 3", progress)

    options = [
        ("Leer Grimorio Web", lambda: read_markdown("03-Laberinto-Web/Grimorio_Web.md")),
        ("Laboratorio: SQL Injection", lambda: run_lab("03-Laberinto-Web/lab_sqli.py")),
        ("Marcar como completado", lambda: mark_world_completed("Mundo 3", progress)),
    ]

    while True:
        choice = world_menu(3, "LABERINTO WEB", options)
        if choice == '0':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            options[int(choice) - 1][1]()
            input(f"\n{bcolors.BOLD}Presiona Enter para continuar...{bcolors.ENDC}")

def play_world_4():
    progress = load_progress()
    mark_world_started("Mundo 4", progress)

    options = [
        ("Leer Manual de Malware", lambda: read_markdown("04-Laboratorio-Binario/Manual_Malware.md")),
        ("Laboratorio: Escaner de Malware", lambda: run_lab("04-Laboratorio-Binario/lab_malware_scan.py")),
        ("Marcar como completado", lambda: mark_world_completed("Mundo 4", progress)),
    ]

    while True:
        choice = world_menu(4, "LABORATORIO BINARIO", options)
        if choice == '0':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            options[int(choice) - 1][1]()
            input(f"\n{bcolors.BOLD}Presiona Enter para continuar...{bcolors.ENDC}")

def play_world_5():
    progress = load_progress()
    mark_world_started("Mundo 5", progress)

    options = [
        ("Leer Deep Dive Buffer Overflow", lambda: read_markdown("05-Taller-Exploits/DeepDive_BufferOverflow.md")),
        ("Laboratorio: Simulador BOF", lambda: run_lab("05-Taller-Exploits/lab_bof_simulator.py")),
        ("Marcar como completado", lambda: mark_world_completed("Mundo 5", progress)),
    ]

    while True:
        choice = world_menu(5, "TALLER DE EXPLOITS", options)
        if choice == '0':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            options[int(choice) - 1][1]()
            input(f"\n{bcolors.BOLD}Presiona Enter para continuar...{bcolors.ENDC}")

def play_world_6():
    progress = load_progress()
    mark_world_started("Mundo 6", progress)

    options = [
        ("Leer Guia WiFi", lambda: read_markdown("06-Mar-Frecuencias/Guia_Wifi.md")),
        ("Laboratorio: Auditoria WiFi", lambda: run_lab("06-Mar-Frecuencias/lab_wifi_audit.py")),
        ("Marcar como completado", lambda: mark_world_completed("Mundo 6", progress)),
    ]

    while True:
        choice = world_menu(6, "MAR DE FRECUENCIAS", options)
        if choice == '0':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            options[int(choice) - 1][1]()
            input(f"\n{bcolors.BOLD}Presiona Enter para continuar...{bcolors.ENDC}")

def play_world_7():
    progress = load_progress()
    mark_world_started("Mundo 7", progress)

    options = [
        ("Leer Manual de Criptografia", lambda: read_markdown("07-Camara-Enigma/Manual_Criptografia.md")),
        ("Laboratorio: Criptografia", lambda: run_lab("07-Camara-Enigma/lab_crypto.py")),
        ("Marcar como completado", lambda: mark_world_completed("Mundo 7", progress)),
    ]

    while True:
        choice = world_menu(7, "CAMARA DEL ENIGMA", options)
        if choice == '0':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            options[int(choice) - 1][1]()
            input(f"\n{bcolors.BOLD}Presiona Enter para continuar...{bcolors.ENDC}")

def play_world_8():
    progress = load_progress()
    mark_world_started("Mundo 8", progress)

    options = [
        ("Leer Guia Legal", lambda: read_markdown("08-Gobernanza/Guia_Legal.md")),
        ("Quiz: Legal y Etica", lambda: run_lab("08-Gobernanza/quiz_legal.py")),
        ("Marcar como completado", lambda: mark_world_completed("Mundo 8", progress)),
    ]

    while True:
        choice = world_menu(8, "GOBERNANZA", options)
        if choice == '0':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            options[int(choice) - 1][1]()
            input(f"\n{bcolors.BOLD}Presiona Enter para continuar...{bcolors.ENDC}")

def run_lab(script_path):
    if os.path.exists(script_path):
        os.system(f"python {script_path}")
    else:
        print(f"{bcolors.WARNING}[!] Laboratorio no disponible aun. Proximamente...{bcolors.ENDC}")

def show_security():
    clear_screen()
    banner()
    print(f"{bcolors.FAIL}{'=' * 50}{bcolors.ENDC}")
    print(f"{bcolors.FAIL}          AVISO LEGAL / LEGAL NOTICE{bcolors.ENDC}")
    print(f"{bcolors.FAIL}{'=' * 50}{bcolors.ENDC}\n")
    read_markdown("DISCLAIMER")
    input(f"\n{bcolors.BOLD}Presiona Enter para continuar...{bcolors.ENDC}")

if __name__ == "__main__":
    while True:
        option = main_menu()
        if option == '1':
            play_world_1()
        elif option == '2':
            play_world_2()
        elif option == '3':
            play_world_3()
        elif option == '4':
            play_world_4()
        elif option == '5':
            play_world_5()
        elif option == '6':
            play_world_6()
        elif option == '7':
            play_world_7()
        elif option == '8':
            play_world_8()
        elif option == '0':
            print(f"{bcolors.OKBLUE}Saliendo del sistema... Adios, Hacker.{bcolors.ENDC}")
            break
        else:
            print(f"{bcolors.FAIL}Comando no reconocido.{bcolors.ENDC}")
            time.sleep(1)
