#!/usr/bin/env python3
"""
Laboratorio: Honeyport - Trampa de Puerto
Simula un honeypot basico que detecta conexiones a puertos no autorizados.
EDUCATIONAL ONLY - Usar solo en entornos controlados.
"""

import socket
import threading
import time
import sys
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def log_event(event_type, ip, port):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {event_type} from {ip}:{port}"
    print(f"{bcolors.FAIL}{log_entry}{bcolors.ENDC}")

    with open("honeyport.log", "a") as f:
        f.write(log_entry + "\n")

def handle_client(conn, addr, honeypot_port):
    print(f"{bcolors.WARNING}[!] Conexion entrante de {addr[0]}:{addr[1]}{bcolors.ENDC}")
    log_event("CONNECTION DETECTED", addr[0], addr[1])

    try:
        conn.send(b"Welcome to the server...\n")
        time.sleep(1)
        conn.send(b"Access denied. This incident has been logged.\n")
        time.sleep(1)
        conn.close()
    except:
        pass

    log_event("CONNECTION CLOSED", addr[0], addr[1])

def start_honeypot(port=12345):
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}")
    print("  ╔══════════════════════════════════════╗")
    print("  ║   HONEYPOT LAB - PUERTO TRAMPA      ║")
    print("  ║   Educational Purpose Only          ║")
    print("  ╚══════════════════════════════════════╝")
    print(f"{bcolors.ENDC}")
    print(f"\n{bcolors.OKGREEN}[+] Iniciando honeypot en puerto {port}...{bcolors.ENDC}")
    print(f"{bcolors.WARNING}[!] Solo para entornos controlados!{bcolors.ENDC}\n")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind(('0.0.0.0', port))
        server.listen(5)
        print(f"{bcolors.OKGREEN}[+] Honeypot activo. Esperando conexiones...{bcolors.ENDC}")
        print(f"{bcolors.WARNING}[!] Presiona Ctrl+C para detener{bcolors.ENDC}\n")

        while True:
            conn, addr = server.accept()
            client_thread = threading.Thread(
                target=handle_client,
                args=(conn, addr, port)
            )
            client_thread.start()

    except KeyboardInterrupt:
        print(f"\n{bcolors.OKBLUE}[+] Deteniendo honeypot...{bcolors.ENDC}")
    except Exception as e:
        print(f"{bcolors.FAIL}[!] Error: {e}{bcolors.ENDC}")
    finally:
        server.close()

if __name__ == "__main__":
    port = 12345
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    start_honeypot(port)
