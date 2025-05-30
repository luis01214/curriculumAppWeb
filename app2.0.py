class Proyecto:
    def __init__(self, titulo, descripcion, tecnologias, tipo, enlace=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.tecnologias = tecnologias
        self.tipo = tipo  # "Personal" o "Institucional"
        self.enlace = enlace

    def mostrar(self):
        print(f"🧩 {self.titulo} ({self.tipo})")
        print(f"   Descripción: {self.descripcion}")
        print(f"   Tecnologías: {', '.join(self.tecnologias)}")
        if self.enlace:
            print(f"   Enlace: {self.enlace}")
        print()


class Perfil:
    def __init__(self, nombre, descripcion, correo, proyectos=[]):
        self.nombre = nombre
        self.descripcion = descripcion
        self.correo = correo
        self.proyectos = proyectos

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def mostrar_portafolio(self):
        print(f"👤 Nombre: {self.nombre}")
        print(f"📧 Correo: {self.correo}")
        print(f"📝 Descripción: {self.descripcion}\n")
        print("📂 Proyectos:\n")

        personales = [p for p in self.proyectos if p.tipo == "Personal"]
        institucionales = [p for p in self.proyectos if p.tipo == "Institucional"]

        print("🔷 Proyectos Personales:")
        for p in personales:
            p.mostrar()

        print("🔶 Proyectos Institucionales:")
        for p in institucionales:
            p.mostrar()


# Ejemplo de uso
if __name__ == "__main__":
    perfil = Perfil(
        nombre="Juan Pérez",
        descripcion="Desarrollador Full Stack con experiencia en aplicaciones web y móviles.",
        correo="juan.perez@example.com"
    )

    perfil.agregar_proyecto(Proyecto(
        titulo="Gestor de Tareas Web",
        descripcion="Aplicación para gestión de tareas con autenticación y panel de usuario.",
        tecnologias=["Python", "Flask", "SQLite"],
        tipo="Personal",
        enlace="https://github.com/juanperez/gestor-tareas"
    ))

    perfil.agregar_proyecto(Proyecto(
        titulo="Sistema de Control Escolar",
        descripcion="Sistema institucional para manejo de calificaciones, asistencias y reportes.",
        tecnologias=["Laravel", "MySQL", "Vue.js"],
        tipo="Institucional"
    ))

    perfil.agregar_proyecto(Proyecto(
        titulo="Sitio web para Lavandería Fuente Azul",
        descripcion="Sitio WordPress con mapa, formulario de contacto y blog.",
        tecnologias=["WordPress", "PHP", "HTML", "CSS"],
        tipo="Institucional"
    ))

    perfil.mostrar_portafolio()
