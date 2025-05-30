import tkinter as tk
from tkinter import ttk, messagebox


class Proyecto:
    def __init__(self, titulo, descripcion, tecnologias, tipo, enlace=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.tecnologias = tecnologias
        self.tipo = tipo
        self.enlace = enlace


class PortafolioApp:
    def __init__(self, root, perfil):
        self.root = root
        self.perfil = perfil
        self.root.title("Portafolio de Proyectos")
        self.crear_interfaz()

    def crear_interfaz(self):
        # Info general del perfil
        tk.Label(self.root, text=f"👤 {self.perfil['nombre']}", font=("Helvetica", 16, "bold")).pack(pady=5)
        tk.Label(self.root, text=f"📧 {self.perfil['correo']}", font=("Helvetica", 12)).pack()
        tk.Label(self.root, text=f"📝 {self.perfil['descripcion']}", font=("Helvetica", 12), wraplength=600).pack(pady=5)

        # Pestañas para proyectos
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=1, fill="both")

        frame_personales = ttk.Frame(notebook)
        frame_institucionales = ttk.Frame(notebook)

        notebook.add(frame_personales, text="🔷 Personales")
        notebook.add(frame_institucionales, text="🔶 Institucionales")

        # Añadir proyectos
        for proyecto in self.perfil['proyectos']:
            frame = frame_personales if proyecto.tipo == "Personal" else frame_institucionales
            self.agregar_proyecto_a_frame(proyecto, frame)

    def agregar_proyecto_a_frame(self, proyecto, frame):
        contenedor = ttk.LabelFrame(frame, text=proyecto.titulo, padding=10)
        contenedor.pack(fill="x", pady=5, padx=10)

        ttk.Label(contenedor, text=f"📄 Descripción: {proyecto.descripcion}", wraplength=500).pack(anchor="w")
        ttk.Label(contenedor, text=f"🛠 Tecnologías: {', '.join(proyecto.tecnologias)}").pack(anchor="w")
        if proyecto.enlace:
            ttk.Label(contenedor, text=f"🔗 Enlace: {proyecto.enlace}", foreground="blue").pack(anchor="w")


# Ejemplo de uso
if __name__ == "__main__":
    perfil = {
        "nombre": "Juan Pérez",
        "correo": "juan.perez@example.com",
        "descripcion": "Desarrollador Full Stack con experiencia en aplicaciones web y móviles.",
        "proyectos": [
            Proyecto("Gestor de Tareas Web", "App de tareas con panel de usuario.",
                     ["Python", "Flask", "SQLite"], "Personal",
                     "https://github.com/juanperez/gestor-tareas"),

            Proyecto("Sistema de Control Escolar", "Sistema para notas y asistencia.",
                     ["Laravel", "MySQL", "Vue.js"], "Institucional"),

            Proyecto("Web Lavandería Fuente Azul", "Sitio WordPress con blog y contacto.",
                     ["WordPress", "PHP", "HTML"], "Institucional")
        ]
    }

    root = tk.Tk()
    app = PortafolioApp(root, perfil)
    root.mainloop()
