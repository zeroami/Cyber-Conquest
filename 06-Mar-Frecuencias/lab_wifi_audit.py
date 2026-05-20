#!/usr/bin/env python3
"""
Laboratorio: Auditoria WiFi - Simulador Educativo
Simula los conceptos de auditoria WiFi sin hardware real.
EDUCATIONAL ONLY - Solo para redes propias o con autorizacion.
"""

import hashlib
import sys
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def simulate_network_scan():
    print(f"{bcolors.HEADER}=== Paso 1: Escaneo de Redes ==={bcolors.ENDC}")
    print("Simulando: airodump-ng wlan0mon\n")

    networks = [
        {"bssid": "AA:BB:CC:DD:EE:01", "ch": 6, "power": -45, "ssid": "MiWiFi_Casa", "security": "WPA2", "clients": 3},
        {"bssid": "AA:BB:CC:DD:EE:02", "ch": 11, "power": -67, "ssid": "RedVecino", "security": "WPA2", "clients": 1},
        {"bssid": "AA:BB:CC:DD:EE:03", "ch": 1, "power": -78, "ssid": "OpenNetwork", "security": "OPEN", "clients": 0},
        {"bssid": "AA:BB:CC:DD:EE:04", "ch": 6, "power": -52, "ssid": "Empresa_WiFi", "security": "WPA3", "clients": 12},
        {"bssid": "AA:BB:CC:DD:EE:05", "ch": 36, "power": -89, "ssid": "IoT_Devices", "security": "WPA2", "clients": 5},
    ]

    print(f"{'BSSID':<20} {'CH':<4} {'PWR':<6} {'SSID':<15} {'SEC':<6} {'CLIENTS'}")
    print("-" * 65)

    for net in networks:
        print(f"{net['bssid']:<20} {net['ch']:<4} {net['power']:<6} {net['ssid']:<15} {net['security']:<6} {net['clients']}")

    print(f"\n{bcolors.OKGREEN}[+] Encontradas {len(networks)} redes{bcolors.ENDC}")
    return networks

def simulate_handshake_capture(target_bssid, channel):
    print(f"\n{bcolors.HEADER}=== Paso 2: Captura de Handshake ==={bcolors.ENDC}")
    print(f"Simulando: airodump-ng -c {channel} --bssid {target_bssid} -w capture wlan0mon\n")

    print(f"[+] Fijando canal {channel}...")
    print(f"[+] Filtrando por BSSID {target_bssid}...")
    print(f"[+] Esperando handshake de 4 vias...")

    for i in range(1, 6):
        print(f"    Mensaje {i}/4 del handshake...")

    print(f"\n{bcolors.OKGREEN}[!] WPA handshake capturado!{bcolors.ENDC}")
    print(f"[+] Guardado en: capture-01.cap")

def simulate_deauth(target_bssid, client_mac):
    print(f"\n{bcolors.HEADER}=== Paso 3: Ataque Deautenticacion ==={bcolors.ENDC}")
    print(f"Simulando: aireplay-ng -0 5 -a {target_bssid} -c {client_mac} wlan0mon\n")

    print(f"[+] Enviando paquetes de deautenticacion...")
    for i in range(1, 6):
        print(f"    Deauth packet {i}/5 enviado")

    print(f"\n{bcolors.WARNING}[!] Cliente desautenticado{bcolors.ENDC}")
    print(f"[!] El cliente se reconectara y capturaremos el handshake")

def simulate_cracking(cap_file, wordlist="rockyou.txt"):
    print(f"\n{bcolors.HEADER}=== Paso 4: Crack del Handshake ==={bcolors.ENDC}")
    print(f"Simulando: aircrack-ng -w {wordlist} {cap_file}\n")

    passwords = [
        "12345678",
        "password",
        "qwerty123",
        "MiContraseña2024!",
        "admin1234",
        "letmein",
    ]

    real_password = "MiContraseña2024!"
    print(f"Probando contraseñas del diccionario...\n")

    for pwd in passwords:
        print(f"  Probando: {pwd}")
        if pwd == real_password:
            print(f"\n{bcolors.OKGREEN}[!] KEY FOUND! [{real_password}]{bcolors.ENDC}")
            return real_password

    return None

def show_wifi_security_tips():
    print(f"\n{bcolors.HEADER}=== COMO PROTEGER TU WiFi ==={bcolors.ENDC}")
    print("""
1. ✅ Usar WPA3 (o WPA2 como minimo)
2. ✅ Contraseña larga (>15 caracteres, mezcla de tipos)
3. ✅ Desactivar WPS (vulnerable a ataques de fuerza bruta)
4. ✅ Actualizar firmware del router
5. ✅ Usar MAC filtering (limitacion, no seguridad real)
6. ✅ Red separada para IoT
7. ✅ Desactivar administracion remota
8. ✅ Cambiar credenciales por defecto del router
9. ✅ Monitorizar dispositivos conectados
10. ✅ Usar VLAN para segmentar la red

VULNERABILIDADES COMUNES:
- WEP: Roto, se crackea en minutos
- WPS: Vulnerable a ataques de fuerza bruta (Reaver)
- Contraseñas por defecto: Facilmente googlables
- Firmware antiguo: Vulnerabilidades conocidas
""")

def main():
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}")
    print("  ╔══════════════════════════════════════╗")
    print("  ║   LAB: WIFI AUDIT SIMULATOR         ║")
    print("  ╚══════════════════════════════════════╝")
    print(f"{bcolors.ENDC}\n")

    print(f"{bcolors.WARNING}⚠️  Esto es una SIMULACION EDUCATIVA{bcolors.ENDC}")
    print(f"{bcolors.WARNING}⚠️  Nunca auditar redes sin autorizacion{bcolors.ENDC}\n")

    networks = simulate_network_scan()

    target = networks[0]
    print(f"\nObjetivo seleccionado: {target['ssid']} ({target['bssid']})")

    simulate_handshake_capture(target['bssid'], target['ch'])
    simulate_deauth(target['bssid'], "FF:FF:FF:FF:FF:FF")
    password = simulate_cracking("capture-01.cap")

    if password:
        print(f"\n{bcolors.FAIL}[!] Demostracion completada: tu WiFi fue crackeada{bcolors.ENDC}")
        print(f"{bcolors.FAIL}[!] Imagina si esta fuera tu red real...{bcolors.ENDC}")

    show_wifi_security_tips()

if __name__ == "__main__":
    main()
