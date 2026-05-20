# Cyber-Conquest: Training Ground

> *"No temas a las maquinas, teme a tu falta de conocimiento sobre ellas."*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/zeroami/Cyber-Conquest)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange.svg)](CONTRIBUTING.md)
[![Disclaimer](https://img.shields.io/badge/Disclaimer-Educational%20Only-red.svg)](DISCLAIMER)

Repositorio central de entrenamiento en Ciberseguridad. Documenta el viaje desde los fundamentos defensivos hasta la explotacion y la gobernanza.

---

## Tabla de Contenidos

- [Mapa de Mundos](#-mapa-de-mundos)
- [Inicio Rapido](#-inicio-rapido)
- [Interfaz de Usuario](#-interfaz-de-usuario)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Guia de Uso](#-guia-de-uso)
- [Herramientas Utilizadas](#-herramientas-utilizadas)
- [Contribuir](#-contribuir)
- [Disclaimer Legal](#-disclaimer-legal)

---

## Mapa de Mundos

### Fase 1: Fundamentos y Defensa

| Mundo | Tematica | Archivo | Estado |
|:---|:---|:---|:---:|
| **Mundo 1** | Defensa y Protocolos | [Manual](./01-Bastion-Protocolo/Manual_Defensa.md) | Completo |
| **Mundo 2** | Ingenieria Social | [Guia](./02-Carnaval-Sombras/Guia_Ingenieria_Social.md) | Completo |
| **Mundo 3** | Hacking Web | [Grimorio](./03-Laberinto-Web/Grimorio_Web.md) | Completo |

### Fase 2: Ofensiva (Red Team)

| Mundo | Tematica | Archivo | Estado |
|:---|:---|:---|:---:|
| **Mundo 4** | Malware y Virus | [Manual](./04-Laboratorio-Binario/Manual_Malware.md) | Completo |
| **Mundo 5** | Exploits & Buffer Overflow | [Deep Dive](./05-Taller-Exploits/DeepDive_BufferOverflow.md) | Completo |
| **Mundo 6** | Hacking WiFi & Radio | [Guia](./06-Mar-Frecuencias/Guia_Wifi.md) | Completo |

### Fase 3: Estrategia y Legalidad

| Mundo | Tematica | Archivo | Estado |
|:---|:---|:---|:---:|
| **Mundo 7** | Criptografia | [Manual](./07-Camara-Enigma/Manual_Criptografia.md) | Completo |
| **Mundo 8** | Gobernanza y Leyes | [Guia Legal](./08-Gobernanza/Guia_Legal.md) | Completo |

---

## Inicio Rapido

### Opcion 1: Aplicacion de Terminal

```bash
# Clonar repositorio
git clone https://github.com/zeroami/Cyber-Conquest.git
cd Cyber-Conquest

# Ejecutar la aplicacion interactiva
python app_hacking.py
```

### Opcion 2: Aplicacion Web (Streamlit)

```bash
# Instalar dependencias
pip install -r requirements.txt

# Lanzar la interfaz web
streamlit run app_streamlit.py
```

### Opcion 3: Docker

```bash
# Construir y ejecutar con Docker
docker compose up -d

# Abrir en navegador: http://localhost:8501
```

---

## Interfaz de Usuario

Cyber-Conquest ofrece dos formas de interactuar con el contenido:

### Terminal (CLI)
- Menu interactivo con colores ASCII
- Navegacion por mundos
- Acceso rapido a manuales y scripts
- Ideal para usuarios de Linux/Kali

### Web (Streamlit)
- Interfaz grafica moderna
- Contenido organizado por fases
- Quizzes interactivos
- Seguimiento de progreso
- Ideal para estudio guiado

---

## Estructura del Proyecto

```
Cyber-Conquest/
├── app_hacking.py           # Aplicacion CLI interactiva
├── app_streamlit.py         # Aplicacion web con Streamlit
├── requirements.txt         # Dependencias Python
├── Dockerfile               # Configuracion Docker
├── docker-compose.yml       # Docker Compose
├── README.md                # Documentacion principal
├── CHANGELOG.md             # Historial de cambios
├── CONTRIBUTING.md          # Guia de contribucion
├── SECURITY.md              # Politica de seguridad
├── LICENSE                  # Licencia MIT
├── DISCLAIMER               # Disclaimer legal (16 idiomas)
│
├── 01-Bastion-Protocolo/
│   ├── Manual_Defensa.md
│   └── lab_honeyport.py     # Laboratorio practico
│
├── 02-Carnaval-Sombras/
│   ├── Guia_Ingenieria_Social.md
│   └── quiz_osint.py        # Quiz OSINT
│
├── 03-Laberinto-Web/
│   ├── Grimorio_Web.md
│   └── lab_sqli.py          # Laboratorio SQLi
│
├── 04-Laboratorio-Binario/
│   ├── Manual_Malware.md
│   └── lab_malware_scan.py  # Escaner de malware
│
├── 05-Taller-Exploits/
│   ├── DeepDive_BufferOverflow.md
│   └── lab_bof_simulator.py # Simulador BOF
│
├── 06-Mar-Frecuencias/
│   ├── Guia_Wifi.md
│   └── lab_wifi_audit.py    # Auditoria WiFi
│
├── 07-Camara-Enigma/
│   ├── Manual_Criptografia.md
│   └── lab_crypto.py        # Laboratorio criptografia
│
└── 08-Gobernanza/
    ├── Guia_Legal.md
    └── quiz_legal.py        # Quiz legal
```

---

## Guia de Uso

### Progreso Recomendado

1. **Empieza por el Mundo 1** - Aprende defensa antes de ataque
2. **Completa cada fase** antes de pasar a la siguiente
3. **Practica en entornos controlados** - VMs aisladas, laboratorios CTF
4. **Usa los quizzes** para verificar tu conocimiento

### Entorno de Laboratorio Recomendado

- **VirtualBox/VMware** con Kali Linux
- **Red aislada** (host-only networking)
- **Snapshots** antes de cada practica
- **Machines vulnerables** de VulnHub o HackTheBox

---

## Herramientas Utilizadas

| Categoria | Herramientas |
|:---|:---|
| **OS** | Kali Linux, Parrot OS |
| **Lenguajes** | Python, Bash, C |
| **Red** | Nmap, Wireshark, Aircrack-ng |
| **Explotacion** | Metasploit, GDB, Pwntools |
| **Web** | Burp Suite, OWASP ZAP |
| **Malware** | YARA, PEStudio, Ghidra |
| **Cripto** | OpenSSL, Hashcat, John |

---

## Contribuir

Las contribuciones son bienvenidas! Lee [CONTRIBUTING.md](CONTRIBUTING.md) para empezar.

- Reporta errores o mejoras
- Anade nuevos mundos o laboratorios
- Mejora la documentacion
- Traduce contenido a otros idiomas

---

## Disclaimer Legal

Este repositorio tiene fines puramente **educativos y academicos**.

El uso de estas tecnicas contra sistemas sin autorizacion previa y por escrito es **ilegal**.

Consulta la [Guia Legal](./08-Gobernanza/Guia_Legal.md) y el [DISCLAIMER](DISCLAIMER) completo antes de ejecutar cualquier script.

---

<div align="center">

**Hecho con por [zeroami](https://github.com/zeroami)**

[![GitHub](https://img.shields.io/badge/GitHub-zeroami-black?style=for-the-badge&logo=github)](https://github.com/zeroami)

</div>
