import streamlit as st

# Datos del portafolio
perfil = {
    "nombre": "Juan Pérez",
    "correo": "juan.perez@example.com",
    "descripcion": "Desarrollador Full Stack con experiencia en aplicaciones web y móviles.",
    "proyectos": [
        {
            "titulo": "Gestor de Tareas Web",
            "descripcion": "App de tareas con panel de usuario.",
            "tecnologias": ["Python", "Flask", "SQLite"],
            "tipo": "Personal",
            "enlace": "https://github.com/juanperez/gestor-tareas"
        },
        {
            "titulo": "Sistema de Control Escolar",
            "descripcion": "Sistema para notas y asistencia.",
            "tecnologias": ["Laravel", "MySQL", "Vue.js"],
            "tipo": "Institucional"
        },
        {
            "titulo": "Web Lavandería Fuente Azul",
            "descripcion": "Sitio WordPress con blog y contacto.",
            "tecnologias": ["WordPress", "PHP", "HTML", "CSS"],
            "tipo": "Institucional"
        }
    ]
}

# Interfaz
st.title(f"📁 Portafolio de {perfil['nombre']}")
st.markdown(f"**📧 Correo:** {perfil['correo']}")
st.markdown(f"**🧾 Descripción:** {perfil['descripcion']}")

st.subheader("🗂 Proyectos")

for proyecto in perfil["proyectos"]:
    st.markdown(f"### {proyecto['titulo']}")
    st.markdown(f"**Tipo:** {proyecto['tipo']}")
    st.write(proyecto["descripcion"])
    st.markdown(f"**Tecnologías:** {', '.join(proyecto['tecnologias'])}")
    if proyecto.get("enlace"):
        st.markdown(f"[🔗 Ver proyecto]({proyecto['enlace']})", unsafe_allow_html=True)
    st.markdown("---")
