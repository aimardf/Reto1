Team Charter Management System - Niger 2.0
Descripción del Proyecto

Aplicación web desarrollada con Streamlit que permite al equipo Niger 2.0 gestionar su carta del equipo (Team Charter). Los miembros pueden visualizarla, firmarla digitalmente y los responsables pueden monitorear el progreso.

Equipo Niger 2.0

Luka Isasa – Desarrollador

Aimar Duarte – Desarrollador

Enrique Morales – Desarrollador

Aimar Redondo – Desarrollador

Oihan Cabada – Desarrollador

Objetivos del Sistema

Gestionar la carta del equipo en charter.json

Mostrarla en una interfaz web simple y profesional

Permitir firmas digitales

Guardar firmas en charter.json

Panel para responsables con métricas de progreso

Funcionalidades

Ver carta completa

Firmar digitalmente con validación de duplicados

Administrar firmas desde un panel con métricas y barra de progreso

Persistencia en tiempo real y feedback visual

Estructura de Archivos
Reto1/
├── charter.json
├── app.py
├── README.md
└── requirements.txt

Uso

Iniciar aplicación con:

streamlit run app.py


Disponible en http://localhost:8501.

Páginas

Ver Carta: misión, objetivos, valores y lista de miembros

Firmar Carta: formulario con validación

Administrar Firmas: métricas en tiempo real y registro de firmas

Historias de Usuario

Miembro del equipo: puede leer y firmar la carta de forma digital.

Responsable del proyecto: puede revisar el estado de firmas y fechas.

Experiencia de Usuario

Tres páginas principales con navegación lateral

Diseño simple, colores consistentes y mensajes claros

Requisitos Cumplidos

Carta del equipo en JSON

Visualización web con Streamlit

Firma digital validada y persistente

Panel de administración con métricas

Código simple y mantenible

Características Destacadas

Arquitectura simple en un solo archivo Python

Sin dependencias complejas

Datos centralizados en JSON

Validaciones robustas y feedback inmediato

Soporte y Contacto

GitHub Issues: Repositorio

Email: contactar a cualquier miembro del equipo

Equipo Niger 2.0 – Proyecto desarrollado para el Reto 1



