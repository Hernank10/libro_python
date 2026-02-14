# 🎓 Plataforma Educativa C.I.P.A.I. - Floridablanca

Este proyecto es la plataforma oficial del **Centro de Innovación Pedagógica para el Bilingüismo Activo e Idiomático (C.I.P.A.I.)**, ubicada en Floridablanca, Santander. Está diseñada para facilitar el aprendizaje de inglés a través de una interfaz bilingüe y módulos interactivos.

---

## 🚀 Tecnologías Utilizadas

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.10)
- **Frontend:** HTML5, CSS3 con [Bootstrap 5.3](https://getbootstrap.com/)
- **API:** RESTful para la gestión de módulos y lecciones.
- **Despliegue:** [PythonAnywhere](https://www.pythonanywhere.com/) con adaptador `a2wsgi`.

---

## 📂 Estructura del Proyecto

```text
cipai_platform/
├── app/                # Lógica del servidor (Python)
│   ├── main.py         # Punto de entrada de FastAPI y rutas
│   ├── database.py     # Base de datos simulada y lógica de datos
│   └── __init__.py     # Marcador de paquete
├── templates/          # Plantillas HTML
│   └── index.html      # Página principal bilingüe
├── static/             # Archivos estáticos
│   └── css/            # Estilos personalizados
├── venv/               # Entorno virtual (excluido en .gitignore)
└── README.md           # Documentación del proyecto
