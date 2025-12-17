import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="CYBER-CONQUEST",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS para dar atmósfera hacker
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
    }
    h1, h2, h3 {
        color: #00ff41 !important;
    }
    .stButton>button {
        color: #0e1117;
        background-color: #00ff41;
        border: 1px solid #00ff41;
    }
    .stButton>button:hover {
        background-color: #00cc33;
        border: 1px solid #00cc33;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.title("💀 CYBER-CONQUEST: Sistema de Entrenamiento")
st.markdown("---")

# Barra lateral - Navegación
st.sidebar.title("🗺️ Mapa del Mundo")
mundo = st.sidebar.radio(
    "Selecciona tu misión:",
    ["Inicio", 
     "1. 🏰 Bastión del Protocolo",
     "2. 🎭 Carnaval de las Sombras",
     "3. 🏛️ Laberinto Web", 
     "4. 🧪 Laboratorio Binario",
     "5. 🔨 Taller de Exploits",
     "6. 🌊 Mar de Frecuencias",
     "7. 🔐 Cripta del Cifrado",
     "8. 👑 Trono de Gobernanza"]
)

# --- LÓGICA DE PÁGINAS ---

if mundo == "Inicio":
    st.header("Bienvenido, Operador.")
    st.write("""
    Has accedido a la interfaz central de Cyber-Conquest. 
    Este sistema consolida el conocimiento de más de 80 volúmenes de seguridad informática.
    
    ### ⚡ Estado del Sistema
    - **Módulos Activos:** 8 Mundos
    - **Nivel de Acceso:** Administrador
    - **Objetivo:** Completar la ruta de certificación virtual.
    """)
    st.info("Selecciona un mundo en el menú lateral para comenzar el despliegue de información.")

elif mundo == "1. 🏰 Bastión del Protocolo":
    st.header("🏰 Mundo 1: El Bastión del Protocolo")
    st.subheader("Redes, Firewalls y Protocolos de Defensa")
    
    tab1, tab2, tab3 = st.tabs(["📂 Archivos de Inteligencia", "⚔️ Simulador de Batalla", "📝 Quiz Rápido"])
    
    with tab1:
        st.markdown("### Conceptos Críticos Interceptados")
        st.write("Datos recuperados de 'Network Security Bible' y manuales de campo.")
        
        with st.expander("🔥 Firewall: Static vs Stateful"):
            st.write("""
            **La diferencia vital:**
            * **Static (Sin estado):** Mira el paquete aislado. ¿IP permitida? Pasa. (Rápido pero tonto).
            * **Stateful (Con estado):** Mira el contexto. ¿Este paquete es respuesta a una petición que YO hice? (Más seguro).
            """)
            
        with st.expander("🚇 VPN (Túneles Seguros)"):
            st.write("""
            Tecnología esencial para WANs. Crea un túnel cifrado sobre una red pública.
            Es la base de la seguridad remota económica y robusta.
            """)

    with tab2:
        st.markdown("### 📡 Escáner de Puertos Activo")
        target_ip = st.text_input("Ingresa IP Objetivo (Simulada):", "192.168.1.1")
        if st.button("Iniciar Escaneo Nmap"):
            st.code(f"""
            Iniciando Nmap 7.92 en {target_ip}...
            PORT     STATE SERVICE
            21/tcp   open  ftp
            22/tcp   open  ssh
            80/tcp   open  http
            Scanning completed in 0.45 seconds
            """, language="bash")
            st.warning("⚠️ ¡Alerta! Puerto FTP (21) detectado abierto. Vector de ataque potencial.")

    with tab3:
        st.write("### Prueba de Conocimiento")
        ans = st.radio("¿Qué protocolo reemplaza a ARP en IPv6?", ["ICMPv6", "Neighbor Discovery (ND)", "IGMP"])
        if st.button("Validar Respuesta"):
            if ans == "Neighbor Discovery (ND)":
                st.success("¡Correcto! ND maneja el descubrimiento de routers y resolución de direcciones.")
            else:
                st.error("Incorrecto. Revisa los archivos de inteligencia.")

# (Aquí puedes añadir más lógica `elif` para los otros mundos más adelante)
else:
    st.warning("🔒 Módulo encriptado. Desbloquea niveles anteriores o contribuye al código para acceder.")
