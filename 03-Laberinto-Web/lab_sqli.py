#!/usr/bin/env python3
"""
Laboratorio: SQL Injection - Simulador Educativo
Simula un entorno de SQL Injection para entender como funciona.
EDUCATIONAL ONLY - Nunca usar contra sistemas reales sin autorizacion.
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class MockDatabase:
    def __init__(self):
        self.users = [
            {"id": 1, "username": "admin", "password": "supersecret123", "role": "admin"},
            {"id": 2, "username": "user1", "password": "password456", "role": "user"},
            {"id": 3, "username": "test", "password": "test123", "role": "user"},
        ]

    def unsafe_query(self, username, password):
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        print(f"{bcolors.WARNING}[QUERY] {query}{bcolors.ENDC}\n")

        for user in self.users:
            if user["username"] == username and user["password"] == password:
                return user
        return None

    def safe_query(self, username, password):
        query = "SELECT * FROM users WHERE username=? AND password=?"
        print(f"{bcolors.OKGREEN}[QUERY] {query}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}[PARAMS] username='{username}', password='***'{bcolors.ENDC}\n")

        for user in self.users:
            if user["username"] == username and user["password"] == password:
                return user
        return None

def demo_sqli():
    db = MockDatabase()

    print(f"{bcolors.OKCYAN}{bcolors.BOLD}")
    print("  ╔══════════════════════════════════════╗")
    print("  ║   LAB: SQL INJECTION SIMULATOR      ║")
    print("  ╚══════════════════════════════════════╝")
    print(f"{bcolors.ENDC}\n")

    print(f"{bcolors.HEADER}=== DEMO 1: Login Normal ==={bcolors.ENDC}")
    print("Intentando login con credenciales validas...\n")
    result = db.unsafe_query("admin", "supersecret123")
    if result:
        print(f"{bcolors.OKGREEN}[✓] Login exitoso: {result['username']} ({result['role']}){bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}[✗] Login fallido{bcolors.ENDC}")

    print(f"\n{bcolors.HEADER}=== DEMO 2: SQL Injection Basico ==={bcolors.ENDC}")
    print("Intentando bypass con SQLi...\n")
    sqli_payload = "' OR '1'='1"
    result = db.unsafe_query("admin", sqli_payload)
    if result:
        print(f"{bcolors.FAIL}[!] SQL Injection exitoso! Acceso como: {result['username']}{bcolors.ENDC}")
    else:
        print(f"{bcolors.OKGREEN}[✓] SQL Injection bloqueado{bcolors.ENDC}")

    print(f"\n{bcolors.HEADER}=== DEMO 3: SQL Injection - UNION ==={bcolors.ENDC}")
    print("Intentando extraer datos con UNION...\n")
    sqli_union = "' UNION SELECT 1,username,password,role FROM users--"
    print(f"{bcolors.WARNING}[!] Payload: {sqli_union}{bcolors.ENDC}")
    print(f"{bcolors.WARNING}[!] Esto extraeria TODOS los usuarios en un ataque real{bcolors.ENDC}")

    print(f"\n{bcolors.HEADER}=== DEMO 4: Consulta Segura (Prepared Statements) ==={bcolors.ENDC}")
    print("Usando parameterized query...\n")
    result = db.safe_query("admin", "' OR '1'='1")
    if result:
        print(f"{bcolors.OKGREEN}[✓] Login exitoso{bcolors.ENDC}")
    else:
        print(f"{bcolors.OKGREEN}[✓] SQL Injection bloqueado por prepared statement{bcolors.ENDC}")

def interactive_lab():
    db = MockDatabase()

    print(f"\n{bcolors.HEADER}=== MODO INTERACTIVO ==={bcolors.ENDC}")
    print("Intenta hacer login. Puedes probar payloads de SQLi.\n")
    print(f"{bcolors.WARNING}Tips para SQLi:{bcolors.ENDC}")
    print("  - ' OR '1'='1")
    print("  - ' OR 1=1--")
    print("  - admin'--")

    while True:
        username = input(f"\n{bcolors.BOLD}Username: {bcolors.ENDC}")
        if username.lower() in ['q', 'quit', 'exit']:
            break

        password = input(f"{bcolors.BOLD}Password: {bcolors.ENDC}")

        result = db.unsafe_query(username, password)
        if result:
            print(f"{bcolors.FAIL}[!] Login como: {result['username']} ({result['role']}){bcolors.ENDC}")
        else:
            print(f"{bcolors.OKGREEN}[✓] Login fallido{bcolors.ENDC}")

def show_defense_tips():
    print(f"\n{bcolors.HEADER}=== COMO DEFENDERSE ==={bcolors.ENDC}")
    print("""
1. ✅ Usar Prepared Statements / Parameterized Queries
2. ✅ Validar y sanitizar inputs
3. ✅ Usar ORM (Object-Relational Mapping)
4. ✅ Principle of Least Privilege en DB
5. ✅ Web Application Firewall (WAF)
6. ✅ Input length limits
7. ✅ Error messages genericos (no revelar estructura DB)
8. ✅ Regular security audits y pentesting
""")

if __name__ == "__main__":
    demo_sqli()
    show_defense_tips()

    choice = input(f"\n{bcolors.BOLD}Quieres probar el modo interactivo? (s/n): {bcolors.ENDC}")
    if choice.lower() == 's':
        interactive_lab()
