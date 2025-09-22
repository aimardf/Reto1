# Team Charter Management System - Niger 2.0

## 📋 Descripción del Proyecto

Este sistema permite al equipo **Niger 2.0** gestionar su carta del equipo (Team Charter) de manera digital mediante una aplicación web desarrollada con **Streamlit**. Los integrantes pueden visualizar la carta completa y firmar digitalmente para aceptar los términos establecidos.

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
5. **Interfaz moderna** - Proporcionar una experiencia de usuario clara y atractiva

## 🚀 Funcionalidades

### ✨ Aplicación Web (Streamlit)
- **🏠 Página de Inicio** - Resumen del equipo y estado general de firmas
- **📜 Ver Carta del Equipo** - Visualización completa y organizada de toda la carta
- **✍️ Firmar Carta** - Sistema de firma digital intuitivo y seguro
- **📊 Estado de Firmas** - Dashboard con progreso y estadísticas detalladas

### 🔧 Características Técnicas
- **Interfaz responsive** - Compatible con dispositivos móviles y desktop
- **Validación de firmas** - Previene firmas duplicadas
- **Persistencia en tiempo real** - Los datos se guardan inmediatamente
- **Feedback visual** - Confirmaciones, alertas y notificaciones claras

## 📁 Estructura de Archivos

```
Reto1/
├── charter.json         # Carta del equipo con firmas integradas
├── app.py              # Aplicación principal Streamlit
├── README.md           # Documentación del proyecto
└── requirements.txt    # Dependencias del proyecto
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
      "timestamp": "2025-09-22T10:30:00.000Z",
      "date": "22/09/2025 10:30:00"
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

#### 🏠 Inicio
- **Información general** del equipo y proyecto
- **Resumen de la misión** del equipo
- **Lista de miembros** con sus roles
- **Indicador de progreso** de firmas

#### 📜 Ver Carta del Equipo
- **Información completa** del equipo Niger 2.0
- **Misión y objetivos** detallados
- **Valores y normas** del equipo
- **Fortalezas y áreas de mejora** identificadas
- **Lista completa** de miembros con roles

#### ✍️ Firmar Carta
- **Formulario de firma** intuitivo
- **Selección de miembro** desde lista desplegable
- **Visualización del email** automática
- **Resumen de la carta** antes de firmar
- **Confirmación de términos** mediante checkbox
- **Validación** contra firmas duplicadas
- **Confirmación visual** al completar la firma

#### 📊 Estado de Firmas
- **Métricas generales** (total miembros, firmados, pendientes, % completado)
- **Barra de progreso** visual
- **Estado detallado** de cada miembro
- **Tabla completa** con fechas de firma
- **Detalles expandibles** de cada firma registrada

## 🎨 Experiencia de Usuario

### Diseño Visual
- **Colores corporativos** azules y profesionales
- **Iconos descriptivos** para mejor comprensión
- **Layout responsive** que se adapta a cualquier pantalla
- **Tipografía clara** y fácil de leer

### Interactividad
- **Navegación mediante sidebar** clara y organizada
- **Formularios intuitivos** con validación en tiempo real
- **Feedback inmediato** con mensajes de éxito, error y advertencia
- **Animaciones celebratorias** al completar firmas (globos)
- **Tablas interactivas** con ordenación y filtrado

### Usabilidad
- **Flujo lógico** desde información hasta firma
- **Prevención de errores** con validaciones apropiadas
- **Mensajes claros** en español para toda la audiencia
- **Confirmaciones** antes de acciones importantes

## 📈 Casos de Uso

### 1. Miembro Nuevo Firma la Carta
1. Acceder a la aplicación web
2. Navegar a "📜 Ver Carta del Equipo" para leer toda la información
3. Ir a "✍️ Firmar Carta"
4. Seleccionar su nombre de la lista
5. Leer el resumen de la carta en el expandidor
6. Marcar el checkbox de aceptación
7. Hacer clic en "Firmar Carta del Equipo"
8. Recibir confirmación visual con animación

### 2. Seguimiento del Progreso del Equipo
1. Acceder a "🏠 Inicio" para ver resumen general
2. Revisar la barra de progreso de firmas
3. Ir a "📊 Estado de Firmas" para detalles completos
4. Verificar qué miembros han firmado y cuáles están pendientes
5. Revisar fechas y detalles de firmas individuales

### 3. Consulta de Información del Equipo
1. Usar "📜 Ver Carta del Equipo" para ver toda la información
2. Revisar misión, objetivos, valores y normas
3. Consultar fortalezas y áreas de mejora
4. Verificar lista completa de miembros y roles

## 🔧 Características Técnicas Avanzadas

### Validaciones Implementadas
- **Prevención de firmas duplicadas** - El sistema verifica emails únicos
- **Validación de selección** - Obliga a seleccionar un miembro válido
- **Confirmación de términos** - Requiere aceptación explícita antes de firmar
- **Manejo de errores** - Gestión graceful de problemas de archivos o datos

### Persistencia de Datos
- **Archivo único** - Toda la información en `charter.json`
- **Timestamps precisos** - Registro de fecha y hora exacta de cada firma
- **Formato legible** - JSON con indentación y codificación UTF-8
- **Respaldo automático** - Los datos se guardan inmediatamente tras cada cambio

### Rendimiento y Escalabilidad
- **Carga eficiente** - Lectura optimizada de archivos JSON
- **Interfaz responsiva** - Actualización automática tras cambios
- **Compatibilidad** - Funciona en navegadores modernos
- **Ligereza** - Dependencias mínimas para máximo rendimiento

## 📋 Requisitos Cumplidos

✅ **Guardar carta del equipo** - `charter.json` con misión, objetivos, roles y normas  
✅ **Mostrar en web** - Interfaz web completa y profesional con Streamlit  
✅ **Firma digital** - Sistema completo de firmas con validación integrada  
✅ **Almacenamiento de firmas** - Firmas guardadas directamente en `charter.json`  
✅ **Interfaz para datos** - Web intuitiva para visualizar y gestionar la carta  
✅ **Proyecto funcional** - Sistema completo y robusto, no prototipo  
✅ **Código ordenado** - Estructura clara, comentarios y documentación completa  
✅ **Participación activa** - Cada miembro puede contribuir a diferentes componentes  
✅ **GitHub** - Repositorio compartido con historial de commits  

## 🌟 Características Destacadas

- **Diseño profesional** - Interfaz moderna y atractiva
- **Experiencia intuitiva** - Flujo de usuario lógico y fácil de seguir
- **Feedback visual completo** - Mensajes claros y animaciones celebratorias
- **Datos unificados** - Todo en un solo archivo JSON para simplicidad
- **Responsive design** - Compatible con móviles, tablets y desktop
- **Multiidioma** - Preparado para español con codificación UTF-8

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