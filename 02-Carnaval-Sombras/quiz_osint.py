#!/usr/bin/env python3
"""
Quiz: OSINT - Reconocimiento de Fuentes Abiertas
Pon a prueba tus conocimientos sobre tecnicas OSINT.
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

questions = [
    {
        "question": "Que es un Google Dork?",
        "options": [
            "Un tipo de malware",
            "Operador de busqueda avanzado de Google",
            "Una herramienta de hacking",
            "Un exploit de Google"
        ],
        "answer": 1,
        "explanation": "Los Google Dorks son operadores avanzados que permiten filtrar resultados de busqueda para encontrar informacion sensible expuesta."
    },
    {
        "question": "Que herramienta permite buscar dispositivos conectados a Internet?",
        "options": [
            "Google",
            "Shodan",
            "Bing",
            "Yahoo"
        ],
        "answer": 1,
        "explanation": "Shodan es un motor de busqueda que escanea Internet y permite encontrar dispositivos IoT, servidores, camaras, etc."
    },
    {
        "question": "Que tipo de informacion pueden contener las fotos (EXIF)?",
        "options": [
            "Solo la fecha",
            "GPS, camara, fecha, configuracion",
            "Solo el nombre del archivo",
            "Nada, son solo pixeles"
        ],
        "answer": 1,
        "explanation": "Los metadatos EXIF pueden revelar coordenadas GPS, modelo de camara, fecha/hora, configuracion de曝光, etc."
    },
    {
        "question": "Que es el 'pretexting' en ingenieria social?",
        "options": [
            "Enviar emails masivos",
            "Crear un escenario falso para obtener informacion",
            "Hackear una base de datos",
            "Instalar malware"
        ],
        "answer": 1,
        "explanation": "El pretexting consiste en crear un escenario o pretexto creible para manipular a la victima y que revele informacion sensible."
    },
    {
        "question": "Que es Maltego?",
        "options": [
            "Un antivirus",
            "Una herramienta de analisis de enlaces y OSINT",
            "Un firewall",
            "Un sistema operativo"
        ],
        "answer": 1,
        "explanation": "Maltego es una herramienta de mineria de datos y analisis visual que permite descubrir relaciones entre personas, empresas, dominios, etc."
    },
    {
        "question": "Cual es el principio de Cialdini que explota la urgencia?",
        "options": [
            "Reciprocidad",
            "Prueba social",
            "Escasez/Urgencia",
            "Autoridad"
        ],
        "answer": 2,
        "explanation": "El principio de Escasez/Urgencia hace que las personas actuen rapido por miedo a perder una oportunidad."
    },
    {
        "question": "Que es un ataque 'USB Drop'?",
        "options": [
            "Dejar USBs infectados en lugares publicos",
            "Hackear por USB directamente",
            "Enviar USB por correo",
            "Vender USB con malware"
        ],
        "answer": 0,
        "explanation": "Un ataque USB Drop consiste en dejar memorias USB infectadas en lugares publicos esperando que alguien las conecte por curiosidad."
    },
    {
        "question": "Que tipo de shredder se recomienda para documentos sensibles?",
        "options": [
            "De tiras (strip-cut)",
            "P-4 o superior (cross-cut)",
            "Cualquiera vale",
            "No hace falta shredder"
        ],
        "answer": 1,
        "explanation": "Se recomienda shredder de corte cruzado nivel P-4 o superior para que los documentos no puedan ser reconstruidos."
    }
]

def run_quiz():
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}")
    print("  ╔══════════════════════════════════════╗")
    print("  ║       QUIZ: OSINT RECONNAISSANCE    ║")
    print("  ╚══════════════════════════════════════╝")
    print(f"{bcolors.ENDC}\n")

    score = 0
    total = len(questions)

    for i, q in enumerate(questions, 1):
        print(f"{bcolors.HEADER}Pregunta {i}/{total}{bcolors.ENDC}")
        print(f"{bcolors.BOLD}{q['question']}{bcolors.ENDC}\n")

        for j, opt in enumerate(q["options"], 1):
            print(f"  {j}. {opt}")

        while True:
            try:
                answer = int(input(f"\n{bcolors.BOLD}Tu respuesta (1-4): {bcolors.ENDC}"))
                if 1 <= answer <= 4:
                    break
                print(f"{bcolors.FAIL}Opcion invalida{bcolors.ENDC}")
            except ValueError:
                print(f"{bcolors.FAIL}Introduce un numero{bcolors.ENDC}")

        if answer - 1 == q["answer"]:
            print(f"{bcolors.OKGREEN}✓ Correcto!{bcolors.ENDC}")
            score += 1
        else:
            print(f"{bcolors.FAIL}✗ Incorrecto{bcolors.ENDC}")

        print(f"{bcolors.OKCYAN}  {q['explanation']}{bcolors.ENDC}\n")
        print("-" * 50)

    print(f"\n{bcolors.HEADER}RESULTADO FINAL{bcolors.ENDC}")
    pct = (score / total) * 100
    print(f"Aciertos: {score}/{total} ({pct:.0f}%)")

    if pct >= 80:
        print(f"{bcolors.OKGREEN}🎉 Excelente! Dominas OSINT!{bcolors.ENDC}")
    elif pct >= 60:
        print(f"{bcolors.WARNING}👍 Bien, pero puedes mejorar.{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}📚 Necesitas repasar el Mundo 2.{bcolors.ENDC}")

if __name__ == "__main__":
    run_quiz()
