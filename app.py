"""
Team Charter Niger 2.0 - Versión Simple
Sistema web para firmar la carta del equipo
"""

import streamlit as st
import json
from datetime import datetime

# Configuración de página
st.set_page_config(page_title="Niger 2.0 - Team Charter", page_icon="🚀")

def load_charter():
    """Carga la carta del equipo"""
    try:
        with open('charter.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        st.error("Error cargando charter.json")
        return None

def save_charter(data):
    """Guarda la carta del equipo"""
    try:
        with open('charter.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except:
        return False

# Título
st.title("Team Charter - Niger 2.0")

# Cargar datos
charter = load_charter()
if not charter:
    st.stop()

# Menú simple
page = st.sidebar.selectbox("Menú", ["Ver Carta", "Firmar", "Administrar Firmas"])

if page == "Ver Carta":
    st.header("Carta del Equipo")
    
    st.subheader(f"{charter['team_name']}")
    
    st.write("**Miembros:**")
    for member in charter['members']:
        st.write(f"• {member['name']} ({member['email']})")
    
    st.write("**Misión:**")
    for item in charter['mission']:
        st.write(f"• {item}")
    
    st.write("**Objetivos:**")
    for item in charter['objectives']:
        st.write(f"• {item}")
    
    st.write("**Valores:**")
    for item in charter['values']:
        st.write(f"• {item}")

elif page == "Firmar":
    st.header("Firmar Carta")
    
    # Mostrar quién ya firmó
    signatures = charter.get('signatures', [])
    if signatures:
        st.write("**Ya firmaron:**")
        for sig in signatures:
            st.write(f"✅ {sig['name']} - {sig['date']}")
    
    # Formulario de firma
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
                # Buscar email
                email = ""
                for member in charter['members']:
                    if member['name'] == selected:
                        email = member['email']
                        break
                
                # Verificar si ya firmó
                ya_firmo = any(sig['email'] == email for sig in signatures)
                
                if ya_firmo:
                    st.warning("Ya has firmado")
                else:
                    # Agregar firma
                    nueva_firma = {
                        "name": selected,
                        "email": email,
                        "agreement": True,
                        "date": datetime.now().strftime("%d/%m/%Y %H:%M")
                    }
                    
                    if 'signatures' not in charter:
                        charter['signatures'] = []
                    
                    charter['signatures'].append(nueva_firma)
                    
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
    
    # Estadísticas rápidas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Miembros", len(members))
    with col2:
        st.metric("Firmaron", len(signatures))
    with col3:
        pendientes = len(members) - len(signatures)
        st.metric("Pendientes", pendientes)
    
    # Progreso visual
    if len(members) > 0:
        progreso = len(signatures) / len(members)
        st.progress(progreso)
        st.write(f"**Progreso:** {len(signatures)}/{len(members)} ({progreso*100:.0f}%)")
    
    # Lista completa de estado
    st.subheader("Estado Completo de Firmas")
    
    for member in members:
        # Buscar si firmó
        firmo = False
        fecha_firma = ""
        
        for sig in signatures:
            if sig['email'] == member['email']:
                firmo = True
                fecha_firma = sig['date']
                break
        
        # Mostrar estado
        if firmo:
            st.success(f"✅ **{member['name']}** ({member['email']}) - Firmó el {fecha_firma}")
        else:
            st.error(f"❌ **{member['name']}** ({member['email']}) - **PENDIENTE**")
    
    # Detalles de firmas registradas
    if signatures:
        st.subheader("Registro Detallado de Firmas")
        st.write("*Información completa para auditoría:*")
        
        for i, sig in enumerate(signatures, 1):
            with st.expander(f"Firma #{i}: {sig['name']}"):
                st.write(f"**Nombre:** {sig['name']}")
                st.write(f"**Email:** {sig['email']}")
                st.write(f"**Fecha y Hora:** {sig['date']}")
                st.write(f"**Aceptación:** {'✅ SÍ' if sig.get('agreement', True) else '❌ NO'}")