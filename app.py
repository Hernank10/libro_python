from flask import Flask, render_template_string

app = Flask(__name__)

# --- CONFIGURACIÓN DE CAPÍTULOS ---
# Aquí puedes pegar los contenidos de tus capítulos anteriores
LIBRO_DATA = {
    "1": {
        "titulo": "Capítulo 1: La Chispa de la Lógica",
        "descripcion": "Fundamentos y el primer 'Hola Mundo'.",
        "contenido": "Programar es como escribir una receta de cocina. Python interpreta nuestras órdenes paso a paso.",
        "codigo": "print('¡Hola, mundo!')\nnombre = 'Explorador'\nprint(f'Bienvenido {nombre}')",
        "color": "blue"
    },
    "2": {
        "titulo": "Capítulo 2: Controlando el Flujo",
        "descripcion": "Condicionales y toma de decisiones.",
        "contenido": "Aprenderemos a usar 'if' para que el código decida qué camino tomar según las condiciones.",
        "codigo": "edad = 18\nif edad >= 18:\n    print('Eres mayor de edad')\nelse:\n    print('Eres menor')",
        "color": "emerald"
    },
    "3": {
        "titulo": "Capítulo 3: Bucles e Iteraciones",
        "descripcion": "Repetición de tareas sin esfuerzo.",
        "contenido": "Los bucles for y while nos permiten repetir acciones miles de veces con pocas líneas de código.",
        "codigo": "for i in range(5):\n    print(f'Repetición número {i+1}')",
        "color": "purple"
    }
    # Para añadir más capítulos, simplemente sigue este formato:
    # "4": { "titulo": "...", "descripcion": "...", ... }
}

BASE_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Libro Python Interactivo</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-50 text-gray-800 min-h-screen flex flex-col">

    <!-- Navbar -->
    <nav class="bg-slate-900 text-white p-4 shadow-xl sticky top-0 z-50">
        <div class="container mx-auto flex justify-between items-center">
            <a href="/" class="text-xl font-bold tracking-widest text-blue-400">
                <i class="fas fa-terminal mr-2"></i>PYTHON BOOK
            </a>
            <div class="hidden md:flex space-x-6 text-sm uppercase tracking-wider font-semibold">
                <a href="/" class="hover:text-blue-400 transition">Inicio</a>
                {% for id, cap in libro.items() %}
                <a href="/capitulo/{{ id }}" class="hover:text-blue-400 transition">Cap {{ id }}</a>
                {% endfor %}
            </div>
        </div>
    </nav>

    <div class="container mx-auto py-10 px-4 max-w-6xl flex-grow">
        <div class="flex flex-col md:flex-row gap-8">
            
            <!-- Sidebar / Índice -->
            <aside class="w-full md:w-1/4">
                <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6 sticky top-24">
                    <h3 class="font-bold text-gray-900 mb-4 border-b pb-2">Índice</h3>
                    <ul class="space-y-3">
                        {% for id, cap_info in libro.items() %}
                        <li>
                            <a href="/capitulo/{{ id }}" class="block p-2 rounded hover:bg-gray-100 text-gray-600 hover:text-blue-600 transition {% if current_id == id %}bg-blue-50 text-blue-700 font-bold border-l-4 border-blue-600{% endif %}">
                                {{ id }}. {{ cap_info.titulo }}
                            </a>
                        </li>
                        {% endfor %}
                    </ul>
                </div>
            </aside>

            <!-- Contenido Principal -->
            <main class="w-full md:w-3/4">
                {% if cap %}
                    <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
                        <div class="bg-{{ cap.color }}-600 p-8 text-white">
                            <span class="bg-white/20 text-xs font-bold px-2 py-1 rounded uppercase tracking-widest">Lección Interactiva</span>
                            <h2 class="text-4xl font-extrabold mt-2">{{ cap.titulo }}</h2>
                            <p class="mt-2 text-{{ cap.color }}-100 text-lg italic opacity-90">{{ cap.descripcion }}</p>
                        </div>
                        
                        <div class="p-8 space-y-8 text-gray-700">
                            <section>
                                <h3 class="text-2xl font-bold mb-4 flex items-center">
                                    <i class="fas fa-book-open mr-3 text-{{ cap.color }}-600"></i>Explicación
                                </h3>
                                <p class="leading-relaxed text-lg">{{ cap.contenido }}</p>
                            </section>

                            <section>
                                <h3 class="text-2xl font-bold mb-4 flex items-center">
                                    <i class="fas fa-code mr-3 text-{{ cap.color }}-600"></i>Código del Programa
                                </h3>
                                <div class="bg-slate-900 rounded-xl p-6 relative shadow-inner">
                                    <pre class="text-green-400 font-mono text-sm overflow-x-auto"><code>{{ cap.codigo }}</code></pre>
                                    <button class="absolute top-4 right-4 text-slate-500 hover:text-white transition">
                                        <i class="fas fa-copy"></i>
                                    </button>
                                </div>
                            </section>
                        </div>
                    </div>
                {% else %}
                    <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-12 text-center space-y-6">
                        <div class="inline-block p-4 bg-blue-50 rounded-full mb-4">
                            <i class="fas fa-rocket text-5xl text-blue-600"></i>
                        </div>
                        <h1 class="text-5xl font-black text-slate-900">Tu Viaje Python</h1>
                        <p class="text-xl text-gray-500 max-w-xl mx-auto">Selecciona un capítulo en el menú de la izquierda para comenzar a integrar tus programas con la teoría.</p>
                        <div class="pt-6">
                            <a href="/capitulo/1" class="bg-blue-600 text-white px-10 py-4 rounded-full text-lg font-bold hover:bg-blue-700 transition shadow-lg inline-block">
                                Empezar desde el inicio
                            </a>
                        </div>
                    </div>
                {% endif %}
            </main>
        </div>
    </div>

    <footer class="bg-white border-t py-8 text-center text-gray-400 text-sm mt-auto">
        <p>&copy; 2024 Libro de Python Interactiva. Alojado en PythonAnywhere.</p>
    </footer>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(BASE_HTML, libro=LIBRO_DATA, cap=None, current_id=None)

@app.route('/capitulo/<id>')
def view_cap(id):
    cap = LIBRO_DATA.get(id)
    return render_template_string(BASE_HTML, libro=LIBRO_DATA, cap=cap, current_id=id)

if __name__ == '__main__':
    app.run(debug=True)
