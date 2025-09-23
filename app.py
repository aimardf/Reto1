import streamlit as st
import json
from datetime import datetime

# Configuración de página
st.set_page_config(page_title="Niger 2.0 - Team Charter")

def load_charter():
    try:
        with open('charter.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        st.error("Error cargando charter.json")
        return None

def save_charter(data):
    try:
        with open('charter.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except:
        return False

st.title("Team Charter - Niger 2.0")
charter = load_charter()
if not charter:
    st.stop()

page = st.sidebar.selectbox("Menú", ["Ver Carta", "Firmar", "Administrar Firmas"])

if page == "Ver Carta":
    st.header("Carta del Equipo")
    st.subheader(f"{charter['team_name']}")

    sections = ["Miembros", "Misión", "Objetivos", "Valores"]
    data = [
        [f"{m['name']} ({m['email']})" for m in charter['members']],
        charter['mission'],
        charter['objectives'],
        charter['values']
    ]

    for title, items in zip(sections, data):
        with st.container():
            st.markdown(f"### {title}")
            for item in items:
                st.write(f"- {item}")
            st.markdown("---")

elif page == "Firmar":
    st.header("Firmar Carta")
    signatures = charter.get('signatures', [])
    if signatures:
        st.write("**Ya firmaron:**")
        for sig in signatures:
            st.success(f"{sig['name']} - Firmó el {sig['date']}")

    with st.form("firma"):
        names = [m['name'] for m in charter['members']]
        selected = st.selectbox("Tu nombre:", ["Selecciona..."] + names)
        agree = st.checkbox("Acepto la carta del equipo")
        submit = st.form_submit_button("Firmar")
        
        if submit:
            if selected == "Selecciona...":
                st.error("Selecciona tu nombre")
            elif not agree:
                st.error("Debes aceptar la carta")
            else:
                email = next((m['email'] for m in charter['members'] if m['name'] == selected), "")
                if any(sig['email'] == email for sig in signatures):
                    st.warning("Ya has firmado")
                else:
                    nueva_firma = {
                        "name": selected,
                        "email": email,
                        "agreement": True,
                        "date": datetime.now().strftime("%d/%m/%Y %H:%M")
                    }
                    charter.setdefault('signatures', []).append(nueva_firma)
                    if save_charter(charter):
                        st.success(f"¡Gracias {selected}! Firma registrada")
                        st.balloons()
                        st.experimental_rerun()
                    else:
                        st.error("Error guardando firma")

elif page == "Administrar Firmas":
    st.header("Panel del Responsable del Proyecto")
    members = charter.get('members', [])
    signatures = charter.get('signatures', [])

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Miembros", len(members))
    col2.metric("Firmaron", len(signatures))
    col3.metric("Pendientes", len(members) - len(signatures))

    if len(members) > 0:
        progreso = len(signatures) / len(members)
        st.progress(progreso)
        st.write(f"**Progreso:** {len(signatures)}/{len(members)} ({progreso*100:.0f}%)")

    st.subheader("Estado Completo de Firmas")
    for member in members:
        firmo = next((sig for sig in signatures if sig['email'] == member['email']), None)
        if firmo:
            st.success(f"✅ {member['name']} ({member['email']}) - Firmó el {firmo['date']}")
        else:
            st.error(f"❌ {member['name']} ({member['email']}) - PENDIENTE")
