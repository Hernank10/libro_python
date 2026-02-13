from flask import Flask, render_template_string, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'hernank10_secret_stable_key'

# --- DATOS DEL CURSO ---
CURSO_DATA = {
    "1": {
        "titulo": "Módulo 1: Pronombres y Sujetos",
        "descripcion": "Identificar quién realiza la acción.",
        "teoria": "En inglés, el sujeto es obligatorio. Usamos I, You, He, She, It, We, They.",
        "codigo_python": "sujeto = 'She'\nprint(f'{sujeto} is learning python')",
        "ejercicio_pregunta": "Traduce el pronombre 'Ella' al inglés:",
        "respuesta_correcta": "she",
        "color": "blue"
    },
    "2": {
        "titulo": "Módulo 2: El Verbo To Be",
        "descripcion": "Ser o Estar.",
        "teoria": "I am, You are, He/She/It is.",
        "codigo_python": "def be(s):\n    return 'is' if s in ['He','She'] else 'are'",
        "ejercicio_pregunta": "Completa: 'They ____ students' (am, is, are):",
        "respuesta_correcta": "are",
        "color": "indigo"
    },
    "3": {
        "titulo": "Módulo 3: Presente Simple",
        "descripcion": "Regla de la 'S'.",
        "teoria": "Añadimos 's' al verbo con He, She, It.",
        "codigo_python": "def hablar(sujeto):\n    return 'talks' if sujeto == 'He' else 'talk'",
        "ejercicio_pregunta": "Traduce 'Él corre' (He ____):",
        "respuesta_correcta": "he runs",
        "color": "emerald"
    },
    "4": {
        "titulo": "Módulo 4: Adjetivos Posesivos",
        "descripcion": "Pertenencia.",
        "teoria": "My, Your, His, Her, Its, Our, Their.",
        "codigo_python": "gender = 'her'\nprint(f'{gender} book')",
        "ejercicio_pregunta": "Traduce 'Su libro' (de ella):",
        "respuesta_correcta": "her book",
        "color": "rose"
    },
    "5": {
        "titulo": "Módulo 5: Presente Continuo",
        "descripcion": "Acciones ahora.",
        "teoria": "To Be + Verbo -ING.",
        "codigo_python": "print('I am ' + 'play' + 'ing')",
        "ejercicio_pregunta": "Traduce 'Estoy comiendo' (I am ____):",
        "respuesta_correcta": "eating",
        "color": "cyan"
    },
    "6": {
        "titulo": "Módulo 6: Auxiliar Do/Does",
        "descripcion": "Preguntas.",
        "teoria": "Do (I/You/We/They) - Does (He/She/It).",
        "codigo_python": "def ask(s):\n    return 'Does' if s == 'She' else 'Do'",
        "ejercicio_pregunta": "¿Auxiliar para 'You'?:",
        "respuesta_correcta": "do",
        "color": "violet"
    },
    "7": {
        "titulo": "Módulo 7: Pasado Simple",
        "descripcion": "Verbos regulares.",
        "teoria": "Se añade -ED al final.",
        "codigo_python": "v = 'walk'\nprint(v + 'ed')",
        "ejercicio_pregunta": "Pasado de 'Play':",
        "respuesta_correcta": "played",
        "color": "amber"
    },
    "8": {
        "titulo": "Módulo 8: Futuro Will",
        "descripcion": "Predicciones.",
        "teoria": "Will + Verbo infinitivo.",
        "codigo_python": "print('I will ' + 'travel')",
        "ejercicio_pregunta": "Traduce 'Yo iré' (I ____ go):",
        "respuesta_correcta": "will",
        "color": "orange"
    },
    "9": {
        "titulo": "Módulo 9: Verbo Can",
        "descripcion": "Habilidades.",
        "teoria": "Can = Poder. No usa 's'.",
        "codigo_python": "print('I can swim')",
        "ejercicio_pregunta": "Traduce 'Yo puedo':",
        "respuesta_correcta": "i can",
        "color": "teal"
    },
    "10": {
        "titulo": "Módulo 10: Estructura Final",
        "descripcion": "Sujeto + Verbo + Objeto.",
        "teoria": "Orden lógico de la oración.",
        "codigo_python": "s, v, o = 'I', 'like', 'Python'\nprint(f'{s} {v} {o}')",
        "ejercicio_pregunta": "Ordena (Love, I, English):",
        "respuesta_correcta": "i love english",
        "color": "slate"
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inglés Python</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-50 font-sans">
    <nav class="bg-slate-900 text-white p-4 shadow-lg">
        <div class="container mx-auto flex justify-between items-center">
            <span class="font-bold text-xl uppercase tracking-tighter">Inglés<span class="text-blue-400">Python</span></span>
            <span class="text-xs bg-blue-500/20 px-3 py-1 rounded-full border border-blue-500/30">Progreso: {{ porcentaje }}%</span>
        </div>
    </nav>

    <div class="container mx-auto px-4 py-8 flex flex-col lg:flex-row gap-6">
        <aside class="w-full lg:w-1/4">
            <div class="bg-white rounded-2xl p-4 shadow-sm border border-gray-200">
                <h3 class="font-bold text-gray-800 mb-3 text-xs uppercase">Capítulos</h3>
                <div class="space-y-1">
                    {% for id, m in curso.items() %}
                    <a href="/modulo/{{ id }}" class="flex items-center p-2 rounded-lg text-sm {% if current_id == id %}bg-blue-600 text-white{% else %}hover:bg-gray-100 text-gray-600{% endif %}">
                        <span class="mr-2 opacity-50">{{ id }}</span>
                        <span class="truncate">{{ m.titulo.split(':')[1] }}</span>
                        {% if id in completados %}<i class="fas fa-check-circle ml-auto text-emerald-400"></i>{% endif %}
                    </a>
                    {% endfor %}
                </div>
            </div>
        </aside>

        <main class="w-full lg:w-3/4">
            {% if mod %}
                <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
                    <div class="bg-{{ mod.color }}-600 p-6 text-white">
                        <h1 class="text-2xl font-bold">{{ mod.titulo }}</h1>
                    </div>
                    <div class="p-6 space-y-6">
                        <div class="bg-gray-50 p-4 rounded-xl border-l-4 border-{{ mod.color }}-500">
                            <h4 class="font-bold text-gray-800 mb-1 italic">Teoría:</h4>
                            <p class="text-gray-600 text-sm">{{ mod.teoria }}</p>
                        </div>
                        <div class="bg-slate-900 rounded-xl p-4">
                            <pre class="text-emerald-400 text-xs overflow-x-auto"><code>{{ mod.codigo_python }}</code></pre>
                        </div>
                        <div class="bg-{{ mod.color }}-50 p-6 rounded-xl border border-{{ mod.color }}-100">
                            <p class="mb-3 text-gray-800 font-medium">{{ mod.ejercicio_pregunta }}</p>
                            <div class="flex gap-2">
                                <input type="text" id="ans" class="flex-grow p-3 rounded-lg border-2 border-gray-200 outline-none focus:border-{{ mod.color }}-400" placeholder="...">
                                <button onclick="check('{{ current_id }}')" class="bg-{{ mod.color }}-600 text-white px-6 rounded-lg font-bold">RUN</button>
                            </div>
                            <div id="msg" class="mt-3 hidden p-3 rounded-lg text-center font-bold text-sm"></div>
                        </div>
                    </div>
                </div>
            {% else %}
                <div class="bg-white rounded-3xl p-10 text-center shadow-sm border border-gray-200">
                    <h1 class="text-4xl font-black text-gray-900 mb-4 tracking-tighter">Aprende Inglés con Lógica Python</h1>
                    <p class="text-gray-500 mb-8">Un método estructurado para dominar la gramática.</p>
                    <a href="/modulo/1" class="bg-slate-900 text-white px-8 py-3 rounded-xl font-bold uppercase tracking-widest text-sm">Empezar Curso</a>
                </div>
            {% endif %}
        </main>
    </div>

    <script>
        function check(id) {
            const val = document.getElementById('ans').value;
            fetch('/verificar', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({id: id, respuesta: val})
            }).then(r => r.json()).then(data => {
                const m = document.getElementById('msg');
                m.className = 'mt-3 p-3 rounded-lg text-center font-bold text-sm ' + (data.status === 'ok' ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700');
                m.textContent = data.status === 'ok' ? '¡Correcto!' : 'Inténtalo de nuevo.';
                m.classList.remove('hidden');
                if(data.status === 'ok') setTimeout(() => window.location.reload(), 1000);
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    completados = session.get('completados', [])
    porcentaje = int((len(completados) / 10) * 100)
    return render_template_string(HTML_TEMPLATE, curso=CURSO_DATA, mod=None, current_id=None, completados=completados, porcentaje=porcentaje)

@app.route('/modulo/<id>')
def view_modulo(id):
    mod = CURSO_DATA.get(id)
    completados = session.get('completados', [])
    porcentaje = int((len(completados) / 10) * 100)
    return render_template_string(HTML_TEMPLATE, curso=CURSO_DATA, mod=mod, current_id=id, completados=completados, porcentaje=porcentaje)

@app.route('/verificar', methods=['POST'])
def verificar():
    data = request.json
    mod_id = data.get('id')
    ans = data.get('respuesta', '').lower().strip()
    mod = CURSO_DATA.get(mod_id)
    if mod and ans == mod['respuesta_correcta'].lower():
        completados = session.get('completados', [])
        if mod_id not in completados:
            completados.append(mod_id)
            session['completados'] = completados
        return jsonify({'status': 'ok'})
    return jsonify({'status': 'error'})

if __name__ == '__main__':
    app.run