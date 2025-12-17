# 💀 CYBER-CONQUEST: La Arena Digital

[![Status](https://img.shields.io/badge/Status-Active-success)]()
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

**Bienvenido a Cyber-Conquest.**

[cite_start]Este repositorio no es solo una colección de notas; es una **plataforma de aprendizaje gamificado** diseñada para estructurar el conocimiento de más de 80 libros fundamentales de seguridad informática[cite: 1].

El objetivo es transformar la teoría estática en una **aventura interactiva** donde cada commit es un paso más hacia la maestría en ciberseguridad.

## 🗺️ El Mapa del Mundo (Roadmap)

El contenido está organizado en 8 "Mundos Temáticos" que cubren desde los fundamentos hasta la gestión ejecutiva de la seguridad:

### 1. 🏰 [El Bastión del Protocolo](./01-Bastion-Protocolo)
* **Enfoque:** Fundamentos de Redes, TCP/IP y Arquitectura.
* **Herramientas:** Wireshark, Nmap.
* [cite_start]**Conceptos Clave:** Filtrado de paquetes (Stateful vs Static), IPv6 y Protocolos de descubrimiento[cite: 9, 13].

### 2. 🎭 [El Carnaval de las Sombras](./02-Carnaval-Sombras)
* **Enfoque:** Ingeniería Social y Seguridad Física.
* **Misiones:** Análisis de pretextos, OSINT y suplantación de identidad.
* [cite_start]**Conceptos Clave:** Psicología del engaño, políticas de acceso físico[cite: 4, 18].

### 3. 🏛️ [El Laberinto de los Datos Ocultos](./03-Laberinto-Web)
* **Enfoque:** Hacking Web y Bases de Datos.
* **Herramientas:** Burp Suite, SQLMap.
* [cite_start]**Conceptos Clave:** Blind SQL Injection, XSS (Cross-Site Scripting) y OWASP Top 10[cite: 6, 41].

### 4. 🧪 [El Laboratorio del Alquimista Binario](./04-Laboratorio-Binario)
* **Enfoque:** Malware, Virus y Reversing.
* **Herramientas:** IDA Pro, Debuggers.
* [cite_start]**Conceptos Clave:** Análisis de bytecode, ofuscación y comportamiento viral[cite: 7, 8].

### 5. 🔨 [El Taller de las Grietas](./05-Taller-Exploits)
* **Enfoque:** Desarrollo de Exploits y Pentesting.
* **Herramientas:** Metasploit Framework, Shellcode.
* [cite_start]**Conceptos Clave:** Buffer Overflow, gestión de memoria (Stack/Heap)[cite: 11, 43].

### 6. 🌊 [El Mar de las Frecuencias](./06-Mar-Frecuencias)
* **Enfoque:** Seguridad Wireless y Radiofrecuencia.
* **Herramientas:** Aircrack-ng, Kismet.
* [cite_start]**Conceptos Clave:** WEP/WPA Cracking, Modo Monitor e inyección de paquetes[cite: 47, 48].

### 7. 🔐 [La Cripta del Cifrado](./07-Cripta-Cifrado)
* **Enfoque:** Criptografía y Túneles Seguros.
* [cite_start]**Conceptos Clave:** VPNs, Esteganografía vs Criptografía, Hashes y PKI[cite: 10, 11].

### 8. 👑 [El Trono de la Gobernanza](./08-Trono-Gobernanza)
* **Enfoque:** Gestión, CISSP y Cumplimiento.
* [cite_start]**Conceptos Clave:** Auditoría, Gestión de Identidades (IAM) y respuesta a incidentes[cite: 45, 46].

---

## 🚀 Instalación de la Plataforma

Este repositorio incluye una aplicación interactiva en Python (`Streamlit`) para navegar el contenido como si fuera un videojuego.

```bash
# Clonar el repositorio
git clone [https://github.com/TU_USUARIO/cyber-conquest.git](https://github.com/TU_USUARIO/cyber-conquest.git)

# Entrar en el directorio
cd cyber-conquest

# Instalar dependencias
pip install -r requirements.txt

# Iniciar la plataforma
streamlit run app_hacking.py
