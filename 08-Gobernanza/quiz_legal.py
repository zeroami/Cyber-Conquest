#!/usr/bin/env python3
"""
Quiz: Legal y Etica en Ciberseguridad
Pon a prueba tus conocimientos sobre leyes, etica y gobernanza.
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
        "question": "Que es un pentest 'White Box'?",
        "options": [
            "Sin ninguna informacion previa",
            "Con informacion completa del objetivo",
            "Solo con la IP del objetivo",
            "Sin autorizacion"
        ],
        "answer": 1,
        "explanation": "En un pentest White Box, el tester tiene acceso completo a la informacion del sistema (codigo fuente, arquitectura, credenciales)."
    },
    {
        "question": "Que documento es ESENCIAL antes de empezar un pentest?",
        "options": [
            "Un contrato de trabajo",
            "Autorizacion por escrito y Rules of Engagement (ROE)",
            "Un email verbal",
            "Nada, si es para aprender"
        ],
        "answer": 1,
        "explanation": "Sin autorizacion por escrito y ROE definidas, cualquier prueba de penetracion es ilegal, incluso con buenas intenciones."
    },
    {
        "question": "Que es el RGPD?",
        "options": [
            "Un protocolo de red",
            "Reglamento General de Proteccion de Datos de la UE",
            "Una herramienta de hacking",
            "Un tipo de firewall"
        ],
        "answer": 1,
        "explanation": "El RGPD (GDPR en ingles) es la regulacion europea de proteccion de datos que afecta a como se maneja la informacion personal."
    },
    {
        "question": "Que es la 'divulgacion responsable' (responsible disclosure)?",
        "options": [
            "Publicar vulnerabilidades en redes sociales",
            "Reportar vulnerabilidades al vendor antes de hacerlas publicas",
            "Vender vulnerabilidades al mejor postor",
            "Ignorar las vulnerabilidades"
        ],
        "answer": 1,
        "explanation": "La divulgacion responsable implica reportar la vulnerabilidad al fabricante, darle tiempo para parchear, y solo despues hacerla publica."
    },
    {
        "question": "Cual es la diferencia entre un hacker White Hat y Black Hat?",
        "options": [
            "El lenguaje de programacion que usan",
            "White Hat actua con autorizacion, Black Hat sin ella",
            "El sistema operativo que usan",
            "No hay diferencia"
        ],
        "answer": 1,
        "explanation": "La diferencia fundamental es la autorizacion y la intencion. White Hat trabaja legalmente para mejorar la seguridad."
    },
    {
        "question": "Que es un 'Grey Hat'?",
        "options": [
            "Un hacker que usa ropa gris",
            "Alguien que hackea sin autorizacion pero sin intencion maliciosa",
            "Un tipo de firewall",
            "Un protocolo de red"
        ],
        "answer": 1,
        "explanation": "Los Grey Hat operan en un area gris: pueden hackear sin autorizacion pero sin danar, aunque sigue siendo ilegal."
    },
    {
        "question": "Que consecuencias puede tener hackear un sistema sin autorizacion?",
        "options": [
            "Ninguna si no te pillan",
            "Prision, multas y antecedentes penales",
            "Solo una advertencia",
            "Depende del pais, pero nunca es grave"
        ],
        "answer": 1,
        "explanation": "El acceso no autorizado a sistemas informaticos es delito en la mayoria de paises, con penas de prision y multas significativas."
    },
    {
        "question": "Que debe incluir un Scope de pentest?",
        "options": [
            "Solo las IPs a testear",
            "Objetivos, limites, tecnicas permitidas, horarios, contactos de emergencia",
            "Solo el precio del servicio",
            "Solo la duracion del test"
        ],
        "answer": 1,
        "explanation": "Un scope completo define que se puede y no se puede hacer, cuando, como, y a quien contactar en caso de problemas."
    },
    {
        "question": "Que es GRC en ciberseguridad?",
        "options": [
            "Un tipo de malware",
            "Governance, Risk, and Compliance (Gobierno, Riesgo y Cumplimiento)",
            "Una herramienta de hacking",
            "Un protocolo de red"
        ],
        "answer": 1,
        "explanation": "GRC es el marco que asegura que una organizacion cumple con regulaciones, gestiona riesgos y tiene buen gobierno de seguridad."
    },
    {
        "question": "Que framework es popular para gestion de riesgos?",
        "options": [
            "TCP/IP",
            "NIST Cybersecurity Framework",
            "OSI Model",
            "Agile"
        ],
        "answer": 1,
        "explanation": "El NIST CSF es uno de los frameworks mas utilizados para gestionar riesgos de ciberseguridad en organizaciones."
    }
]

def run_quiz():
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}")
    print("  ╔══════════════════════════════════════╗")
    print("  ║   QUIZ: LEGAL & ETHICS              ║")
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
        print(f"{bcolors.OKGREEN}🎉 Excelente! Conoces bien la legalidad!{bcolors.ENDC}")
    elif pct >= 60:
        print(f"{bcolors.WARNING}👍 Bien, pero repasa la guia legal.{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}📚 URGENTE: Lee el Mundo 8 antes de practicar nada!{bcolors.ENDC}")

if __name__ == "__main__":
    run_quiz()
