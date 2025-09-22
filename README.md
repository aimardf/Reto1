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

1. **Gestionar la carta del equipo** - Almacenar misión, objetivos, roles y normas en `charter.json`
2. **Visualización web** - Mostrar la carta en una interfaz web intuitiva y profesional
3. **Firma digital** - Permitir que cada integrante firme digitalmente la carta
4. **Persistencia integrada** - Guardar firmas directamente en `charter.json`
5. **Panel de administración** - Permitir al responsable monitorear el progreso de firmas

## 🚀 Funcionalidades

### ✨ Aplicación Web (Streamlit)
- **📜 Ver Carta** - Visualización completa y organizada de toda la carta del equipo
- **✍️ Firmar Carta** - Sistema de firma digital intuitivo y seguro para miembros
- **�‍💼 Administrar Firmas** - Panel del responsable para monitorear progreso y exportar datos

### 🔧 Características Técnicas
- **Interfaz simple** - Solo 3 páginas principales, fácil de navegar
- **Validación de firmas** - Previene firmas duplicadas
- **Persistencia en tiempo real** - Los datos se guardan inmediatamente
- **Exportación CSV** - Para análisis y auditoría externa
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
  "norms": ["Norma 1", "Norma 2"],
  "strengths": ["Fortaleza 1", "Fortaleza 2"],
  "weaknesses": ["Debilidad 1", "Debilidad 2"],
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
- **Valores y normas** del equipo
- **Lista de miembros** con emails

#### ✍️ Firmar Carta
- **Lista de firmantes** actuales
- **Formulario simple** de firma
- **Selección por nombre** desde lista desplegable
- **Checkbox de aceptación** obligatorio
- **Validación** contra firmas duplicadas
- **Confirmación visual** con animación de globos

#### �‍💼 Administrar Firmas (Panel del Responsable)
- **Métricas en tiempo real** (total, firmados, pendientes, % progreso)
- **Barra de progreso** visual
- **Estado detallado** de cada miembro (firmado/pendiente)
- **Registro completo** de firmas con fechas y horas
- **Exportación a CSV** para auditoría externa

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
- Exportación CSV para análisis externo

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
4. **Responsable** exporta datos cuando sea necesario

## 📋 Requisitos Cumplidos

✅ **Guardar carta del equipo** - `charter.json` con misión, objetivos, roles y normas  
✅ **Mostrar en web** - Interfaz web simple y funcional con Streamlit  
✅ **Firma digital** - Sistema completo de firmas con validación  
✅ **Almacenamiento de firmas** - Firmas guardadas directamente en `charter.json`  
✅ **Interfaz para datos** - Web intuitiva para visualizar y gestionar  
✅ **Panel de administración** - Vista especial para responsables del proyecto  
✅ **Exportación de datos** - CSV para auditoría y análisis externo  
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

## 🔧 Características Técnicas

### Validaciones Implementadas
- **Verificación de archivos** - Manejo de errores si no existen los archivos JSON
- **Validación de formato JSON** - Control de errores de sintaxis
- **Prevención de firmas duplicadas** - No permite firmar dos veces al mismo miembro
- **Validación de entrada** - Control de datos vacíos o inválidos

### Manejo de Errores
- **Archivos no encontrados** - Creación automática de archivos vacíos
- **JSON malformado** - Mensajes de error claros y recuperación graceful
- **Errores de escritura** - Validación antes de guardar cambios
- **Interrupciones de usuario** - Manejo de Ctrl+C en consola

### Persistencia de Datos
- **Formato JSON** - Fácil lectura y escritura de datos estructurados
- **Codificación UTF-8** - Soporte completo para caracteres especiales
- **Backup automático** - Los datos se guardan inmediatamente tras cambios
- **Timestamps** - Registro de fecha y hora en todas las firmas

## 🎨 Diseño y Experiencia de Usuario

### Interfaz Web
- **Diseño responsive** - Funciona en desktop, tablet y móvil
- **Navegación intuitiva** - Menú lateral claro y organizado
- **Feedback visual** - Mensajes de éxito, error y advertencia
- **Iconos descriptivos** - Mejora la comprensión visual
- **Colores corporativos** - Diseño profesional y atractivo

### Interfaz de Consola
- **Menús claros** - Opciones numeradas y bien organizadas
- **Feedback inmediato** - Confirmaciones y mensajes de estado
- **Navegación simple** - Proceso paso a paso para todas las funciones
- **Emojis descriptivos** - Mejora la experiencia visual en terminal

## 📈 Casos de Uso

### 1. Nuevo Miembro del Equipo
1. Ejecutar la aplicación web o consola
2. Ir a "Ver Carta" para leer la carta completa
3. Usar "Firmar Carta" para aceptar digitalmente los términos
4. Verificar la firma en "Firmas Registradas"

### 2. Actualización de la Carta
1. Acceder a "Editar Carta" (web) o opción 2 (consola)
2. Modificar las secciones necesarias
3. Guardar los cambios
4. Notificar al equipo de los cambios realizados

### 3. Revisión de Progreso
1. Usar "Firmas Registradas" para ver quién ha firmado
2. Revisar estadísticas de aceptación
3. Exportar datos para reportes externos
4. Hacer seguimiento a miembros pendientes

### 4. Gestión de Datos
1. Exportar firmas a CSV para análisis externo
2. Hacer backup de charter.json y signatures.json
3. Revisar logs de actividad por timestamps
4. Mantener histórico de cambios

## 🤝 Contribución y Desarrollo

### Estructura del Código
- **Separación de responsabilidades** - Clases específicas para cada funcionalidad
- **Código reutilizable** - Funciones comunes entre interfaces
- **Documentación completa** - Docstrings en todas las funciones
- **Manejo de errores robusto** - Try-catch en operaciones críticas

### Para Contribuir
1. Hacer fork del repositorio
2. Crear rama para nueva funcionalidad
3. Implementar cambios con tests
4. Crear pull request con descripción detallada
5. Revisar y aprobar por el equipo

### Estándares de Código
- **PEP 8** - Estilo de código Python estándar
- **Type hints** - Tipado estático para mejor legibilidad
- **Docstrings** - Documentación en español para todas las funciones
- **Comentarios claros** - Explicaciones en puntos complejos

## 🔒 Consideraciones de Seguridad

- **Validación de entrada** - Filtrado de datos de usuario
- **Manejo seguro de archivos** - Prevención de inyecciones de path
- **Codificación UTF-8** - Manejo correcto de caracteres especiales
- **Sin datos sensibles** - No se almacenan contraseñas o información privada

## 📋 Requisitos Cumplidos

✅ **Guardar carta del equipo** - charter.json con misión, objetivos, roles y normas  
✅ **Mostrar en consola y web** - Dos interfaces completamente funcionales  
✅ **Firma digital** - Sistema completo de firmas con validación  
✅ **Almacenamiento de firmas** - signatures.json con formato estructurado  
✅ **Interfaz para datos** - Web y consola para introducir y gestionar datos  
✅ **Proyecto funcional** - Sistema completo, no prototipo  
✅ **Código ordenado** - Estructura clara y bien documentada  
✅ **Participación activa** - Cada miembro puede contribuir a diferentes partes  
✅ **GitHub** - Repositorio compartido con historial de commits  

## 🌟 Características Adicionales

- **Exportación CSV** - Para análisis externo de firmas
- **Estadísticas en tiempo real** - Dashboard con métricas del equipo
- **Interfaz responsive** - Compatible con dispositivos móviles
- **Manejo de errores robusto** - Recuperación graceful ante fallos
- **Documentación completa** - README detallado y código documentado

## 📞 Soporte y Contacto

Para dudas, sugerencias o reportar problemas:
- **GitHub Issues**: [Crear issue en el repositorio](https://github.com/aimardf/Reto1/issues)
- **Email del equipo**: Contactar a cualquier miembro del equipo Niger 2.0

---

**Equipo Niger 2.0** - Proyecto desarrollado para el Reto 1  
*Comprometidos con la excelencia y el trabajo en equipo* 🚀