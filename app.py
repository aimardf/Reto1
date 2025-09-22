"""
Team Charter Management System - Niger 2.0
Sistema de Gestión de Carta de Equipo

Aplicación web con Streamlit para gestionar la carta del equipo Niger 2.0
y permitir firmas digitales de los integrantes.

Autores: Equipo Niger 2.0
"""

import streamlit as st
import json
from datetime import datetime
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Niger 2.0 - Team Charter",
    page_icon="🚀",
    layout="wide"
)

def load_charter():
    """Carga la carta del equipo desde el archivo JSON"""
    try:
        with open('charter.json', 'r', encoding='utf-8') as file:
            charter = json.load(file)
        
        # Asegurar que existe el campo signatures
        if 'signatures' not in charter:
            charter['signatures'] = []
            save_charter(charter)
        
        return charter
    except FileNotFoundError:
        st.error("Archivo charter.json no encontrado")
        return {}
    except json.JSONDecodeError:
        st.error("Error al leer el archivo charter.json")
        return {}

def save_charter(charter_data):
    """Guarda la carta del equipo en el archivo JSON"""
    try:
        with open('charter.json', 'w', encoding='utf-8') as file:
            json.dump(charter_data, file, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        st.error(f"Error al guardar la carta: {str(e)}")
        return False

def add_signature(charter_data, name, email, agreement):
    """Añade una nueva firma a la carta del equipo"""
    try:
        signatures = charter_data.get('signatures', [])
        
        # Verificar si ya existe una firma de esta persona
        for signature in signatures:
            if signature['email'] == email:
                st.warning(f"{name} ya ha firmado la carta del equipo")
                return False
        
        # Crear nueva firma
        new_signature = {
            "name": name,
            "email": email,
            "agreement": agreement,
            "timestamp": datetime.now().isoformat(),
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        # Añadir la firma
        signatures.append(new_signature)
        charter_data['signatures'] = signatures
        
        # Guardar la carta actualizada
        return save_charter(charter_data)
        
    except Exception as e:
        st.error(f"Error al guardar la firma: {str(e)}")
        return False

st.markdown("""
<h1 style='text-align: center; color: #1f77b4;'>
     Team Charter - Niger 2.0
</h1>
<hr style='margin-bottom: 2rem;'>
""", unsafe_allow_html=True)

# Imagen debajo del título
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <img src= https://upload.wikimedia.org/wikipedia/commons/f/f4/Flag_of_Niger.svg
         alt="Team Charter" style="width: 15%; height: auto;">
</div>
""", unsafe_allow_html=True)

# Cargar datos de la carta
charter_data = load_charter()

if not charter_data:
    st.error("No se pudo cargar la carta del equipo")
    st.stop()

# Navegación con tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Inicio", "📜 Ver Carta", "✍️ Firmar Carta", "📊 Estado de Firmas"])

# TAB 1: INICIO
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("¡Bienvenido al Sistema de Team Charter!")
        
        st.markdown(f"""
        ### 🎯 Equipo: **{charter_data.get('team_name', 'N/A')}**
        
        Este sistema te permite:
        
        - 📖 **Ver la carta del equipo** completa con misión, objetivos y normas
        - ✍️ **Firmar digitalmente** para aceptar los términos de la carta
        - 📊 **Revisar el estado** de firmas de todos los miembros del equipo
        
        ### 🎯 Misión del Equipo
        """)
        
        mission = charter_data.get('mission', [])
        for item in mission:
            st.write(f"• {item}")
    
    with col2:
        st.markdown("### 👥 Miembros del Equipo")
        members = charter_data.get('members', [])
        for member in members:
            st.write(f"• **{member.get('name', 'N/A')}**")
            st.write(f"  📧 {member.get('email', 'N/A')}")
        
        # Estado de firmas resumido
        signatures = charter_data.get('signatures', [])
        total_members = len(members)
        signed_members = len(signatures)
        
        st.markdown("### 📊 Estado de Firmas")
        if total_members > 0:
            progress = signed_members / total_members
            st.progress(progress)
            st.write(f"**{signed_members}/{total_members}** miembros han firmado")

# TAB 2: VER CARTA
with tab2:
    st.header("📜 Carta del Equipo Niger 2.0")
    
    # Información básica del equipo
    st.markdown(f"""
    <div style='background-color: #f0f2f6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;'>
        <h3>🎯 {charter_data.get('team_name', 'N/A')}</h3>
        <p><strong>Número de Miembros:</strong> {len(charter_data.get('members', []))}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Miembros del equipo
    st.subheader("👥 Miembros del Equipo")
    members = charter_data.get('members', [])
    if members:
        df_members = pd.DataFrame(members)
        st.dataframe(df_members, use_container_width=True, hide_index=True)
    
    # Contenido organizado en columnas
    col1, col2 = st.columns(2)
    
    with col1:
        # Misión
        st.subheader("🎯 Misión")
        mission = charter_data.get('mission', [])
        for item in mission:
            st.write(f"• {item}")
        
        # Valores
        st.subheader("💎 Valores")
        values = charter_data.get('values', [])
        for item in values:
            st.write(f"• {item}")
        
        # Fortalezas
        st.subheader("💪 Fortalezas")
        strengths = charter_data.get('strengths', [])
        for item in strengths:
            st.write(f"• {item}")
    
    with col2:
        # Objetivos
        st.subheader("🎯 Objetivos")
        objectives = charter_data.get('objectives', [])
        for item in objectives:
            st.write(f"• {item}")
        
        # Normas
        st.subheader("📋 Normas del Equipo")
        norms = charter_data.get('norms', [])
        for item in norms:
            st.write(f"• {item}")
        
        # Áreas de Mejora
        st.subheader("⚠️ Áreas de Mejora")
        weaknesses = charter_data.get('weaknesses', [])
        for item in weaknesses:
            st.write(f"• {item}")

# TAB 3: FIRMAR CARTA
with tab3:
    st.header("✍️ Firmar Carta del Equipo")
    
    # Información sobre la firma
    st.markdown("""
    <div style='background-color: #e8f4f8; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;'>
        <h4>📝 Acerca de la Firma Digital</h4>
        <p>Al firmar esta carta, confirmas que:</p>
        <ul>
            <li>Has leído y entendido todos los términos de la carta del equipo</li>
            <li>Aceptas cumplir con la misión, objetivos, valores y normas establecidas</li>
            <li>Te comprometes a participar activamente en el proyecto</li>
            <li>Respetarás las decisiones tomadas por el equipo</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Mostrar quién ya ha firmado
    signatures = charter_data.get('signatures', [])
    if signatures:
        st.subheader("✅ Miembros que ya han firmado:")
        for sig in signatures:
            status_icon = "✅" if sig.get('agreement', False) else "❌"
            st.write(f"{status_icon} **{sig['name']}** - {sig['date']}")
        st.markdown("---")
    
    # Formulario de firma
    st.subheader("📝 Formulario de Firma")
    
    with st.form("firma_digital", clear_on_submit=True):
        # Seleccionar miembro del equipo
        members = charter_data.get('members', [])
        member_options = ["Selecciona tu nombre..."] + [f"{member['name']}" for member in members]
        
        selected_member_name = st.selectbox(
            "👤 Selecciona tu nombre:",
            member_options
        )
        
        # Encontrar el email del miembro seleccionado
        selected_email = ""
        if selected_member_name != "Selecciona tu nombre...":
            for member in members:
                if member['name'] == selected_member_name:
                    selected_email = member['email']
                    break
            
            st.write(f"📧 **Email:** {selected_email}")
        
        # Mostrar resumen de la carta
        with st.expander("📖 Ver Resumen de la Carta antes de Firmar"):
            st.write(f"**🎯 Equipo:** {charter_data.get('team_name', 'N/A')}")
            
            st.write("**🎯 Misión:**")
            for item in charter_data.get('mission', []):
                st.write(f"• {item}")
            
            st.write("**📋 Objetivos principales:**")
            for item in charter_data.get('objectives', [])[:3]:
                st.write(f"• {item}")
        
        # Checkbox de acuerdo
        agreement = st.checkbox(
            "✅ **Acepto los términos de la carta del equipo y me comprometo a cumplir con ellos**",
            value=False
        )
        
        # Botón de envío
        submitted = st.form_submit_button(
            "✍️ **Firmar Carta del Equipo**",
            type="primary",
            use_container_width=True
        )
        
        if submitted:
            if selected_member_name == "Selecciona tu nombre...":
                st.error("❌ Por favor, selecciona tu nombre de la lista")
            elif not agreement:
                st.error("❌ Debes aceptar los términos para firmar la carta")
            else:
                # Verificar si ya firmó
                already_signed = any(sig['email'] == selected_email for sig in signatures)
                
                if already_signed:
                    st.warning(f"⚠️ {selected_member_name} ya ha firmado la carta del equipo")
                else:
                    # Guardar firma
                    if add_signature(charter_data, selected_member_name, selected_email, agreement):
                        st.success(f"🎉 ¡Gracias **{selected_member_name}**! Tu firma ha sido registrada exitosamente.")
                        st.balloons()
                        st.rerun()

# TAB 4: ESTADO DE FIRMAS
with tab4:
    st.header("📊 Estado de Firmas del Equipo")
    
    members = charter_data.get('members', [])
    signatures = charter_data.get('signatures', [])
    
    # Estadísticas generales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("👥 Total Miembros", len(members))
    
    with col2:
        signed_count = len(signatures)
        st.metric("✅ Firmas Registradas", signed_count)
    
    with col3:
        pending_count = len(members) - signed_count
        st.metric("⏳ Pendientes", pending_count)
    
    with col4:
        completion_rate = (signed_count / len(members)) * 100 if members else 0
        st.metric("📈 % Completado", f"{completion_rate:.1f}%")
    
    # Barra de progreso
    st.subheader("📊 Progreso de Firmas")
    if len(members) > 0:
        progress = signed_count / len(members)
        st.progress(progress)
    
    # Estado detallado de cada miembro
    st.subheader("👥 Estado Detallado por Miembro")
    
    # Crear lista de estados
    member_status = []
    
    for member in members:
        # Buscar si este miembro ha firmado
        signed = False
        signature_date = ""
        
        for sig in signatures:
            if sig['email'] == member['email']:
                signed = True
                signature_date = sig['date']
                break
        
        status_info = {
            "Nombre": member['name'],
            "Email": member['email'],
            "Estado": "✅ Firmado" if signed else "⏳ Pendiente",
            "Fecha de Firma": signature_date if signed else "-"
        }
        member_status.append(status_info)
    
    # Mostrar tabla
    if member_status:
        df_status = pd.DataFrame(member_status)
        st.dataframe(df_status, use_container_width=True, hide_index=True)
    
    # Detalles de las firmas registradas
    if signatures:
        st.subheader("📋 Detalles de Firmas Registradas")
        
        for i, sig in enumerate(signatures, 1):
            with st.expander(f"✍️ Firma #{i}: {sig['name']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Nombre:** {sig['name']}")
                    st.write(f"**Email:** {sig['email']}")
                with col2:
                    st.write(f"**Fecha:** {sig['date']}")
                    status = "✅ Aceptó" if sig.get('agreement', False) else "❌ Rechazó"
                    st.write(f"**Estado:** {status}")
    
    # Mensaje motivacional
    if signed_count == len(members):
        st.success("🎉 ¡Felicitaciones! Todos los miembros del equipo han firmado la carta.")
        st.balloons()
    elif signed_count > 0:
        remaining = len(members) - signed_count
        st.info(f"👏 ¡Excelente progreso! Faltan {remaining} miembro(s) por firmar la carta.")
    else:
        st.warning("📢 Aún no hay firmas registradas. ¡Anima a tu equipo a firmar la carta!")