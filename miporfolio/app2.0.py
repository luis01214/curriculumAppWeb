from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
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
                "titulo": "Sitio web Lavandería Fuente Azul",
                "descripcion": "Web en WordPress con blog y contacto.",
                "tecnologias": ["WordPress", "PHP", "HTML", "CSS"],
                "tipo": "Institucional"
            }
        ]
    }
    return render_template("index.html", perfil=perfil)

if __name__ == "__main__":
    app.run(debug=True)
