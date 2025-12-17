import streamlit as st
import pandas as pd
import time

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="CYBER-CONQUEST",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Hacker
st.markdown("""
    <style>
    .stApp {background-color: #0e1117; color: #00ff41; font-family: 'Courier New', Courier, monospace;}
    h1, h2, h3 {color: #00ff41 !important;}
    .stButton>button {color: #0e1117; background-color: #00ff41; border: 1px solid #00ff41;}
    .stButton>button:hover {background-color: #00cc33; border: 1px solid #00cc33;}
    .stTextInput>div>div>input {color: #00ff41; background-color: #111;}
    </style>
    """, unsafe_allow_html=True)

st.title("💀 CYBER-CONQUEST: Sistema de Entrenamiento")
st.markdown("---")

# --- NAVEGACIÓN ---
st.sidebar.title("🗺️ Mapa del Mundo")
mundo = st.sidebar.radio(
    "Selecciona tu misión:",
    ["Inicio", 
     "1. 🏰 Bastión del Protocolo", 
     "2. 🎭 Carnaval de las Sombras",
     "3. 🏛️ Laberinto Web", 
     "4. 🧪 Laboratorio Binario",
     "5. 🔨 Taller de Exploits"]
)

# --- MUNDO 1: REDES ---
if mundo == "1. 🏰 Bastión del Protocolo":
    st.header("🏰 Mundo 1: Defensa de Red")
    tab1, tab2 = st.tabs(["📂 Teoría", "⚔️ Escáner Nmap"])
    
    with tab1:
        st.markdown("### 🛡️ Firewalls: Stateful vs Stateless")
        st.info("Stateless: Mira el paquete aislado.\nStateful: Mira el contexto de la conexión.")
        st.markdown("### 🚇 VPN")
        st.write("Túneles cifrados para proteger datos en redes públicas.")

    with tab2:
        st.subheader("Simulador de Escaneo")
        ip = st.text_input("IP Objetivo:", "192.168.1.50")
        if st.button("Escanear"):
            with st.spinner("Enviando sondas SYN..."):
                time.sleep(1)
            st.code(f"""
            PORT   STATE SERVICE
            22/tcp open  ssh
            80/tcp open  http
            """, language="bash")
            st.warning("⚠️ Puerto 80 sin cifrar detectado.")

# --- MUNDO 2: INGENIERÍA SOCIAL ---
elif mundo == "2. 🎭 Carnaval de las Sombras":
    st.header("🎭 Mundo 2: Ingeniería Social")
    st.subheader("El arte del engaño humano")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🕵️‍♂️ Principios de Cialdini")
        st.write("* **Autoridad:** 'Soy el CEO, hazlo ya'.")
        st.write("* **Urgencia:** 'Tu cuenta será borrada en 1 hora'.")
        st.write("* **Escasez:** 'Últimos 2 tickets disponibles'.")
    
    with col2:
        st.markdown("### 📧 Reto: Detecta el Phishing")
        st.code("""
        De: soport@g0ogle.com
        Asunto: ALERTA DE SEGURIDAD
        Haga clic aquí para verificar su contraseña:
        http://bit.ly/secure-google-login
        """, language="text")
        
        opcion = st.radio("¿Es este correo legítimo?", ["Sí", "No, mira el remitente", "No, mira el enlace", "B y C son correctas"])
        if st.button("Analizar Correo"):
            if opcion == "B y C son correctas":
                st.balloons()
                st.success("¡CORRECTO! 'g0ogle.com' es typo-squating y el enlace es sospechoso.")
            else:
                st.error("Fallaste. Has sido hackeado.")

# --- MUNDO 3: HACKING WEB ---
elif mundo == "3. 🏛️ Laberinto Web":
    st.header("🏛️ Mundo 3: Inyección SQL")
    st.markdown("El servidor interpreta tu input como código.")
    
    st.subheader("💉 Laboratorio: SQL Injection (Login Bypass)")
    st.write("Objetivo: Entrar como 'admin' sin saber la contraseña.")
    
    usuario = st.text_input("Usuario:", placeholder="Intenta: admin' OR '1'='1")
    password = st.text_input("Contraseña:", type="password")
    
    # Simulador de Backend SQL Vulnerable
    query = f"SELECT * FROM users WHERE user = '{usuario}' AND pass = '{password}'"
    
    st.markdown("**Consulta que ejecuta el servidor:**")
    st.code(query, language="sql")
    
    if st.button("Login"):
        if "OR '1'='1" in usuario or "OR 1=1" in usuario:
            st.success("🔓 ¡ACCESO CONCEDIDO! Has manipulado la lógica booleana.")
            st.json({"id": 1, "user": "admin", "role": "root", "secret": "FLAG{SQLI_MASTER}"})
        elif usuario == "admin" and password == "1234":
             st.warning("Acceso denegado. Contraseña incorrecta.")
        else:
            st.error("Acceso denegado.")

# --- MUNDO 5: EXPLOITS (Deep Dive) ---
elif mundo == "5. 🔨 Taller de Exploits":
    st.header("🔨 Mundo 5: Buffer Overflows")
    st.write("Este módulo contiene material avanzado extraído de 'The Shellcoder's Handbook'.")
    with st.expander("📖 Ver Anatomía del Stack"):
        st.code("""
        [ High Memory ]
        +----------------+
        | Return Address |  <-- OBJETIVO (EIP)
        +----------------+
        |   Saved EBP    |
        +----------------+
        |   Buffer A     |  <-- Entrada de datos
        +----------------+
        [ Low Memory  ]
        """, language="text")
        st.write("Si escribes más datos de los que caben en Buffer A, sobrescribes EBP y luego RET.")

elif mundo == "Inicio":
    st.write("Bienvenido al sistema central. Selecciona una misión.")
    st.progress(0)

else:
    st.info("🚧 Módulo en construcción. Revisa los archivos .md en el repositorio.")
