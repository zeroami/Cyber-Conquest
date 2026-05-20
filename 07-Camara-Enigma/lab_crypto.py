#!/usr/bin/env python3
"""
Laboratorio: Criptografia - Cifrado Cesar y mas
Implementa algoritmos criptograficos basicos para entender los conceptos.
EDUCATIONAL ONLY.
"""

import hashlib
import base64
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def brute_force_caesar(text):
    print(f"\n{bcolors.HEADER}Ataque de fuerza bruta al Cifrado Cesar:{bcolors.ENDC}\n")
    for shift in range(1, 26):
        decrypted = caesar_decrypt(text, shift)
        print(f"  Shift {shift:2d}: {decrypted}")

def demo_hashing():
    print(f"{bcolors.HEADER}=== Demo: Funciones Hash ==={bcolors.ENDC}")

    messages = [
        "Hola Mundo",
        "hola mundo",
        "Hola Mundo!",
    ]

    print(f"\n{'Mensaje':<15} {'MD5':<35} {'SHA-256 (primeros 16 chars)'}")
    print("-" * 75)

    for msg in messages:
        md5 = hashlib.md5(msg.encode()).hexdigest()
        sha256 = hashlib.sha256(msg.encode()).hexdigest()
        print(f"{msg:<15} {md5:<35} {sha256[:16]}...")

    print(f"\n{bcolors.WARNING}Nota: Un cambio minimo cambia el hash completamente (efecto avalancha){bcolors.ENDC}")

def demo_base64():
    print(f"\n{bcolors.HEADER}=== Demo: Codificacion Base64 ==={bcolors.ENDC}")

    text = "Cyber-Conquest: Training Ground"
    encoded = base64.b64encode(text.encode()).decode()
    decoded = base64.b64decode(encoded).decode()

    print(f"Original:  {text}")
    print(f"Base64:    {encoded}")
    print(f"Decodificado: {decoded}")

    print(f"\n{bcolors.WARNING}Base64 NO es encryption, es solo encoding!{bcolors.ENDC}")
    print(f"Cualquiera puede decodificarlo sin clave.")

def interactive_caesar():
    print(f"\n{bcolors.HEADER}=== Modo Interactivo: Cifrado Cesar ==={bcolors.ENDC}")

    while True:
        print(f"\n1. Cifrar")
        print(f"2. Descifrar")
        print(f"3. Fuerza bruta")
        print(f"0. Salir")

        choice = input(f"\n{bcolors.BOLD}Opcion: {bcolors.ENDC}")

        if choice == '0':
            break
        elif choice == '3':
            text = input("Texto cifrado: ")
            brute_force_caesar(text)
        else:
            text = input("Texto: ")
            shift = int(input("Shift (1-25): "))

            if choice == '1':
                result = caesar_encrypt(text, shift)
                print(f"{bcolors.OKGREEN}Cifrado: {result}{bcolors.ENDC}")
            elif choice == '2':
                result = caesar_decrypt(text, shift)
                print(f"{bcolors.OKGREEN}Descifrado: {result}{bcolors.ENDC}")

def crypto_challenges():
    print(f"\n{bcolors.HEADER}=== Desafios Criptograficos ==={bcolors.ENDC}\n")

    challenges = [
        {
            "type": "caesar",
            "encrypted": "Khoor Zruog",
            "answer": "Hello World",
            "hint": "Shift de 3"
        },
        {
            "type": "caesar",
            "encrypted": "uryyb jbeyq",
            "answer": "hello world",
            "hint": "ROT13 (shift 13)"
        },
        {
            "type": "base64",
            "encrypted": "Q3liZXItQ29ucXVlc3Q=",
            "answer": "Cyber-Conquest",
            "hint": "Base64"
        },
    ]

    score = 0
    for i, challenge in enumerate(challenges, 1):
        print(f"Desafio {i}: {challenge['encrypted']}")
        print(f"Pista: {challenge['hint']}")

        answer = input("Tu respuesta: ")
        if answer == challenge["answer"]:
            print(f"{bcolors.OKGREEN}✓ Correcto!{bcolors.ENDC}")
            score += 1
        else:
            print(f"{bcolors.FAIL}✗ Incorrecto. Respuesta: {challenge['answer']}{bcolors.ENDC}")
        print()

    print(f"Resultado: {score}/{len(challenges)}")

def show_crypto_concepts():
    print(f"\n{bcolors.HEADER}=== Conceptos Criptograficos ==={bcolors.ENDC}")
    print("""
SIMETRICA (AES, DES, ChaCha20):
- Misma clave para cifrar y descifrar
- Rapida, ideal para grandes volumenes
- Uso: Disk encryption, VPNs, WiFi

ASIMETRICA (RSA, ECC, ElGamal):
- Par de claves: publica y privada
- Mas lenta, pero resuelve problema de distribucion de claves
- Uso: HTTPS, firmas digitales, Bitcoin

HASHING (SHA-256, MD5, bcrypt):
- Un solo sentido, irreversible
- Tamano fijo independientemente del input
- Uso: Passwords, integridad de archivos, blockchain

ENCODING (Base64, Hex, URL encoding):
- NO es criptografia!
- Solo cambia el formato de representacion
- Cualquiera puede decodificar sin clave
""")

if __name__ == "__main__":
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}")
    print("  ╔══════════════════════════════════════╗")
    print("  ║   LAB: CRYPTOGRAPHY LAB             ║")
    print("  ╚══════════════════════════════════════╝")
    print(f"{bcolors.ENDC}\n")

    print(f"{bcolors.HEADER}=== Cifrado Cesar ==={bcolors.ENDC}")
    original = "Hello World"
    shift = 3
    encrypted = caesar_encrypt(original, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print(f"Original:  {original}")
    print(f"Shift:     {shift}")
    print(f"Cifrado:   {encrypted}")
    print(f"Descifrado: {decrypted}")

    demo_hashing()
    demo_base64()
    show_crypto_concepts()

    choice = input(f"\n{bcolors.BOLD}Quieres el modo interactivo? (s/n): {bcolors.ENDC}")
    if choice.lower() == 's':
        interactive_caesar()
        crypto_challenges()
