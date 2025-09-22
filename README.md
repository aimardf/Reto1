# Team Charter Management System - Niger 2.0

## 📋 Descripción del Proyecto

Este sistema permite al equipo **Niger 2.0** gestionar su carta del equipo (Team Charter) de manera digital mediante una aplicación web desarrollada con **Streamlit**. Los integrantes pueden visualizar la carta completa, firmar digitalmente para aceptar los términos, y los responsables pueden monitorear el progreso.

## 👥 Equipo Niger 2.0

- **Luka Isasa** (isasanovic4@gmail.com) - Desarrollador
- **Aimar Duarte** (aimardfcole@gmail.com) - Desarrollador  
- **Enrique Morales** (emoralescebanc@gmail.com) - Desarrollador
- **Aimar Redondo** (aredondocebanc@gmail.com) - Desarrollador
- **Oihan Cabada** (oihan.cebanc1@gmail.com) - Desarrollador

## 🎯 Objetivos del Sistema

1. **Gestionar la carta del equipo** - Almacenar misión, objetivos y valores en `charter.json`
2. **Visualización web** - Mostrar la carta en una interfaz web intuitiva y profesional
3. **Firma digital** - Permitir que cada integrante firme digitalmente la carta
4. **Persistencia integrada** - Guardar firmas directamente en `charter.json`
5. **Panel de administración** - Permitir al responsable monitorear el progreso de firmas

## 🚀 Funcionalidades

### ✨ Aplicación Web (Streamlit)
- **📜 Ver Carta** - Visualización completa y organizada de toda la carta del equipo
- **✍️ Firmar Carta** - Sistema de firma digital intuitivo y seguro para miembros
- **👨‍💼 Administrar Firmas** - Panel del responsable para monitorear progreso de firmas

### 🔧 Características Técnicas
- **Interfaz simple** - Solo 3 páginas principales, fácil de navegar
- **Validación de firmas** - Previene firmas duplicadas
- **Persistencia en tiempo real** - Los datos se guardan inmediatamente
- **Feedback visual** - Confirmaciones, alertas y métricas claras

## 📁 Estructura de Archivos

```
Reto1/
├── charter.json         # Carta del equipo con firmas integradas
├── app.py              # Aplicación principal Streamlit (simple)
├── README.md           # Documentación del proyecto
└── requirements.txt    # Dependencias mínimas
```

## 📊 Formato de Datos

### charter.json (Estructura completa)
```json
{
  "team_name": "Niger 2.0",
  "members": [
    {"name": "Nombre", "email": "email@domain.com", "role": "Desarrollador"}
  ],
  "mission": ["Punto 1 de la misión", "Punto 2 de la misión"],
  "objectives": ["Objetivo 1", "Objetivo 2"],
  "values": ["Valor 1", "Valor 2"],
  "signatures": [
    {
      "name": "Nombre del miembro",
      "email": "email@domain.com",
      "agreement": true,
      "date": "22/09/2025 10:30"
    }
  ]
}
```

## 🛠️ Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/aimardf/Reto1.git
cd Reto1
```

2. **Crear entorno virtual (recomendado)**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## 🚀 Uso del Sistema

### Iniciar la Aplicación Web

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### 📱 Páginas Disponibles

#### 📜 Ver Carta
- **Información completa** del equipo Niger 2.0
- **Misión y objetivos** detallados
- **Valores** del equipo
- **Lista de miembros** con emails

#### ✍️ Firmar Carta
- **Lista de firmantes** actuales
- **Formulario simple** de firma
- **Selección por nombre** desde lista desplegable
- **Checkbox de aceptación** obligatorio
- **Validación** contra firmas duplicadas
- **Confirmación visual** con animación de globos

#### 👨‍💼 Administrar Firmas (Panel del Responsable)
- **Métricas en tiempo real** (total, firmados, pendientes, % progreso)
- **Barra de progreso** visual
- **Estado detallado** de cada miembro (firmado/pendiente)
- **Registro completo** de firmas con fechas y horas

## 📈 Historias de Usuario Implementadas

### Historia de Usuario 1 - Miembro del Equipo
**COMO** miembro del equipo,  
**QUIERO** leer la carta del equipo y firmarla digitalmente,  
**PARA** confirmar que acepto los términos y comprometerme con el proyecto.

✅ **Criterios cumplidos:**
- El miembro puede leer toda la carta antes de firmar
- Formulario simple con nombre y checkbox de aceptación
- Solo se permite una firma por miembro
- Confirmación visual al completar la firma

### Historia de Usuario 2 - Responsable del Proyecto
**COMO** responsable del proyecto,  
**QUIERO** que la aplicación guarde y muestre todas las firmas de los miembros,  
**PARA** poder comprobar quién ha aceptado la carta y quién no.

✅ **Criterios cumplidos:**
- Panel específico para ver lista completa de firmas
- Identificación clara de quién firmó y cuándo
- Información guardada en charter.json (JSON)
- Solo se aceptan firmas válidas con nombre y aceptación marcada

## 🎨 Experiencia de Usuario

### Diseño Simple y Funcional
- **3 páginas principales** claramente diferenciadas
- **Navegación lateral** intuitiva
- **Iconos descriptivos** para mejor comprensión
- **Colores consistentes** azules y verdes para éxito

### Flujo de Trabajo
1. **Miembro** accede a "Ver Carta" para leer toda la información
2. **Miembro** va a "Firmar Carta" y completa el formulario
3. **Responsable** revisa progreso en "Administrar Firmas"

## 📋 Requisitos Cumplidos

✅ **Guardar carta del equipo** - `charter.json` con misión, objetivos y valores  
✅ **Mostrar en web** - Interfaz web simple y funcional con Streamlit  
✅ **Firma digital** - Sistema completo de firmas con validación  
✅ **Almacenamiento de firmas** - Firmas guardadas directamente en `charter.json`  
✅ **Interfaz para datos** - Web intuitiva para visualizar y gestionar  
✅ **Panel de administración** - Vista especial para responsables del proyecto  
✅ **Código simple** - Solo 150 líneas de código, fácil de mantener  
✅ **GitHub** - Repositorio compartido con historial de commits  

## 🌟 Características Destacadas

- **Arquitectura simple** - Un solo archivo Python con lógica clara
- **Sin dependencias complejas** - Solo Streamlit como framework
- **Datos centralizados** - Todo en charter.json para máxima simplicidad
- **Interfaz responsiva** - Funciona en cualquier dispositivo
- **Validaciones robustas** - Previene errores y duplicados
- **Feedback inmediato** - Mensajes claros y animaciones

## 📞 Soporte y Contacto

Para dudas, sugerencias o reportar problemas:
- **GitHub Issues**: [Crear issue en el repositorio](https://github.com/aimardf/Reto1/issues)
- **Email del equipo**: Contactar a cualquier miembro del equipo Niger 2.0

---

**Equipo Niger 2.0** - Proyecto desarrollado para el Reto 1  
*Comprometidos con la excelencia y el trabajo en equipo* 🚀