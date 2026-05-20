import streamlit as st
import os
import json
from datetime import datetime

st.set_page_config(
    page_title="Cyber-Conquest",
    page_icon="🚩",
    layout="wide",
    initial_sidebar_state="expanded"
)

PROGRESS_FILE = "progress.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"completed": [], "started": [], "last_access": None}

def save_progress(progress):
    progress["last_access"] = datetime.now().isoformat()
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)

def read_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return "Archivo no encontrado."

def main():
    st.sidebar.title("🚩 Cyber-Conquest")
    st.sidebar.markdown("---")

    progress = load_progress()
    completed = len(progress.get("completed", []))

    st.sidebar.metric("Mundos completados", f"{completed}/8")

    if completed > 0:
        pct = (completed / 8) * 100
        st.sidebar.progress(pct / 100)

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Fases")
    st.sidebar.markdown("🟢 **Fase 1:** Fundamentos")
    st.sidebar.markdown("🔴 **Fase 2:** Ofensiva")
    st.sidebar.markdown("🔵 **Fase 3:** Estrategia")

    st.title("🚩 Cyber-Conquest: Training Ground")
    st.markdown('> *"No temas a las maquinas, teme a tu falta de conocimiento sobre ellas."*')

    tab1, tab2, tab3, tab4 = st.tabs(["🟢 Fase 1", "🔴 Fase 2", "🔵 Fase 3", "📊 Progreso"])

    with tab1:
        st.header("Fase 1: Fundamentos y Defensa")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("🛡️ Mundo 1: Bastion y Protocolo")
            st.markdown("Defensa de red, firewalls, VPNs, hardening")
            if st.button("Abrir Mundo 1", key="w1"):
                st.session_state.current_world = 1
            if "Mundo 1" in progress.get("completed", []):
                st.success("✓ Completado")

        with col2:
            st.subheader("🎭 Mundo 2: Carnaval de Sombras")
            st.markdown("Ingenieria social, OSINT, psicología")
            if st.button("Abrir Mundo 2", key="w2"):
                st.session_state.current_world = 2
            if "Mundo 2" in progress.get("completed", []):
                st.success("✓ Completado")

        with col3:
            st.subheader("🕸️ Mundo 3: Laberinto Web")
            st.markdown("SQLi, XSS, hacking web")
            if st.button("Abrir Mundo 3", key="w3"):
                st.session_state.current_world = 3
            if "Mundo 3" in progress.get("completed", []):
                st.success("✓ Completado")

    with tab2:
        st.header("Fase 2: Ofensiva (Red Team)")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("🦠 Mundo 4: Laboratorio Binario")
            st.markdown("Analisis de malware, sandbox")
            if st.button("Abrir Mundo 4", key="w4"):
                st.session_state.current_world = 4
            if "Mundo 4" in progress.get("completed", []):
                st.success("✓ Completado")

        with col2:
            st.subheader("🧪 Mundo 5: Taller de Exploits")
            st.markdown("Buffer overflow, explotacion")
            if st.button("Abrir Mundo 5", key="w5"):
                st.session_state.current_world = 5
            if "Mundo 5" in progress.get("completed", []):
                st.success("✓ Completado")

        with col3:
            st.subheader("📡 Mundo 6: Mar de Frecuencias")
            st.markdown("WiFi hacking, radio, Aircrack-ng")
            if st.button("Abrir Mundo 6", key="w6"):
                st.session_state.current_world = 6
            if "Mundo 6" in progress.get("completed", []):
                st.success("✓ Completado")

    with tab3:
        st.header("Fase 3: Estrategia y Legalidad")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔐 Mundo 7: Camara del Enigma")
            st.markdown("Criptografia, cifrado, hashing")
            if st.button("Abrir Mundo 7", key="w7"):
                st.session_state.current_world = 7
            if "Mundo 7" in progress.get("completed", []):
                st.success("✓ Completado")

        with col2:
            st.subheader("⚖️ Mundo 8: Gobernanza")
            st.markdown("Leyes, etica, GRC")
            if st.button("Abrir Mundo 8", key="w8"):
                st.session_state.current_world = 8
            if "Mundo 8" in progress.get("completed", []):
                st.success("✓ Completado")

    with tab4:
        st.header("📊 Tu Progreso")
        st.metric("Mundos completados", f"{completed}/8")
        if completed > 0:
            st.progress(completed / 8)
            st.markdown(f"**{completed/8*100:.0f}%** completado")

        if progress.get("completed"):
            st.subheader("Completados")
            for w in progress["completed"]:
                st.success(f"✓ {w}")

        if progress.get("started"):
            in_progress = [w for w in progress["started"] if w not in progress.get("completed", [])]
            if in_progress:
                st.subheader("En progreso")
                for w in in_progress:
                    st.warning(f"◐ {w}")

    if "current_world" in st.session_state:
        world = st.session_state.current_world
        world_data = {
            1: ("Mundo 1: Bastion y Protocolo", "01-Bastion-Protocolo/Manual_Defensa.md", "Mundo 1"),
            2: ("Mundo 2: Carnaval de Sombras", "02-Carnaval-Sombras/Guia_Ingenieria_Social.md", "Mundo 2"),
            3: ("Mundo 3: Laberinto Web", "03-Laberinto-Web/Grimorio_Web.md", "Mundo 3"),
            4: ("Mundo 4: Laboratorio Binario", "04-Laboratorio-Binario/Manual_Malware.md", "Mundo 4"),
            5: ("Mundo 5: Taller de Exploits", "05-Taller-Exploits/DeepDive_BufferOverflow.md", "Mundo 5"),
            6: ("Mundo 6: Mar de Frecuencias", "06-Mar-Frecuencias/Guia_Wifi.md", "Mundo 6"),
            7: ("Mundo 7: Camara del Enigma", "07-Camara-Enigma/Manual_Criptografia.md", "Mundo 7"),
            8: ("Mundo 8: Gobernanza", "08-Gobernanza/Guia_Legal.md", "Mundo 8"),
        }

        if world in world_data:
            title, filepath, world_id = world_data[world]
            st.header(title)

            if st.button("← Volver"):
                del st.session_state.current_world
                st.rerun()

            content = read_file(filepath)
            st.markdown(content)

            col1, col2 = st.columns(2)
            with col1:
                if st.button("📖 Marcar como leido"):
                    progress = load_progress()
                    if world_id not in progress["started"]:
                        progress["started"].append(world_id)
                    save_progress(progress)
                    st.success("Marcado como leido!")
                    st.rerun()
            with col2:
                if st.button("✅ Marcar como completado"):
                    progress = load_progress()
                    if world_id not in progress["started"]:
                        progress["started"].append(world_id)
                    if world_id not in progress["completed"]:
                        progress["completed"].append(world_id)
                    save_progress(progress)
                    st.success("Mundo completado! 🎉")
                    st.rerun()

if __name__ == "__main__":
    main()
