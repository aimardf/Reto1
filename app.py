import streamlit as st
import json
from datetime import datetime

# Configuración de página
st.set_page_config(page_title="Niger 2.0 - Team Charter", layout="wide")

# -----------------------
# Funciones de gestión
# -----------------------
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

def load_competencias():
    try:
        with open('competencias.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_competencias(competencias):
    try:
        with open('competencias.json', 'w', encoding='utf-8') as f:
            json.dump(competencias, f, indent=2, ensure_ascii=False)
        return True
    except:
        return False

def save_competencia(nombre, email, bloque, que_se, que_necesito):
    competencias = load_competencias()
    nueva_competencia = {
        "nombre": nombre,
        "email": email,
        "bloque": bloque,
        "que_se": que_se,
        "que_necesito": que_necesito,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    competencias.append(nueva_competencia)
    return save_competencias(competencias)

def export_to_csv():
    competencias = load_competencias()
    if not competencias:
        return None
    
    csv_content = "nombre,email,bloque,que_se,que_necesito,fecha\n"
    for comp in competencias:
        csv_content += f'"{comp["nombre"]}","{comp["email"]}","{comp["bloque"]}","{comp["que_se"]}","{comp["que_necesito"]}","{comp["fecha"]}"\n'
    return csv_content

# -----------------------
# Cargar datos
# -----------------------
st.title("Team Charter - Niger 2.0")
charter = load_charter()
if not charter:
    st.stop()

# -----------------------
# Barra de pestañas
# -----------------------
tabs = ["Ver Carta", "Firmar", "Administrar Firmas", "Añadir formulario", "Ver formularios"]
tab_objs = st.tabs(tabs)

# -----------------------
# Pestaña 1: Ver Carta
# -----------------------
with tab_objs[0]:
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

# -----------------------
# Pestaña 2: Firmar
# -----------------------
with tab_objs[1]:
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
                        st.rerun()
                    else:
                        st.error("Error guardando firma")

# -----------------------
# Pestaña 3: Administrar Firmas
# -----------------------
with tab_objs[2]:
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

# -----------------------
# Pestaña 4: Añadir formulario
# -----------------------
with tab_objs[3]:
    st.header("Formulario de Competencias")
    competencias_list = [
        "ERP / Odoo",
        "Docker / Contenedores", 
        "Base de Datos (Postgres)",
        "Integraciones (Java / otros)",
        "Gestión del Proyecto",
        "Infraestructura / DevOps",
        "Comunicación oral",
        "Comunicación escrita",
        "Trabajo en equipo",
        "Competencia personal"
    ]

    with st.form("formulario_competencias"):
        names = [m['name'] for m in charter['members']]
        selected_member = st.selectbox("Tu nombre:", ["Selecciona..."] + names)
        bloque = st.selectbox("Selecciona una competencia:", ["Selecciona..."] + competencias_list)
        col1, col2 = st.columns(2)
        with col1:
            que_se = st.text_area("Qué sé (fortalezas):", height=100)
        with col2:
            que_necesito = st.text_area("Qué necesito aprender:", height=100)
        
        submitted = st.form_submit_button("Guardar")
        
        if submitted:
            if selected_member == "Selecciona...":
                st.error("Selecciona tu nombre")
            elif bloque == "Selecciona...":
                st.error("Selecciona una competencia")
            elif not que_se.strip() and not que_necesito.strip():
                st.error("Completa al menos uno de los campos")
            else:
                email = next((m['email'] for m in charter['members'] if m['name'] == selected_member), "")
                if save_competencia(selected_member, email, bloque, que_se.strip(), que_necesito.strip()):
                    st.success("Competencia guardada correctamente")
                    st.balloons()
                else:
                    st.error("Error al guardar")

# -----------------------
# Pestaña 5: Ver formularios
# -----------------------
with tab_objs[4]:
    st.header("Competencias del Equipo")
    competencias = load_competencias()
    
    if not competencias:
        st.info("No hay competencias registradas aún")
    else:
        csv_data = export_to_csv()
        if csv_data:
            st.download_button(
                label="Descargar CSV",
                data=csv_data,
                file_name=f"competencias_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv"
            )
        
        st.write(f"**Total de competencias registradas: {len(competencias)}**")
        
        for idx, comp in enumerate(competencias):
            with st.expander(f"{comp['nombre']} - {comp['bloque']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Qué sé:**")
                    st.write(comp['que_se'] if comp['que_se'] else "No especificado")
                with col2:
                    st.write("**Qué necesito aprender:**")
                    st.write(comp['que_necesito'] if comp['que_necesito'] else "No especificado")
                st.caption(f"Registrado: {comp['fecha']}")
                if st.button("Borrar", key=f"borrar_{idx}"):
                    competencias.pop(idx)
                    save_competencias(competencias)
                    st.success("Competencia eliminada")
                    st.rerun()
