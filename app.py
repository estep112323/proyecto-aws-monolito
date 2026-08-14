from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)


registros = []


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Aplicación Monolítica - Examen</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); max-width: 500px; margin: 0 auto; }
        h1 { color: #333; }
        input[type="text"] { width: 70%; padding: 8px; margin-right: 5px; }
        button { padding: 8px 15px; background: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; }
        ul { list-style-type: none; padding: 0; }
        li { background: #e9ecef; margin: 5px 0; padding: 10px; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Sistema de Registro (Monolito)</h1>
        
        <!-- FUNCIONALIDAD 1: Registrar -->
        <h3>1. Registrar Nuevo Elemento</h3>
        <form action="/agregar" method="POST">
            <input type="text" name="nuevo_dato" placeholder="Escribe algo aquí..." required>
            <button type="submit">Guardar</button>
        </form>

        <hr>

        <!-- FUNCIONALIDAD 2: Consultar -->
        <h3>2. Consultar Registros</h3>
        {% if registros %}
            <ul>
                {% for item in registros %}
                    <li>{{ item }}</li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No hay registros guardados aún.</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def inicio():
    # Muestra la lista de registros (Funcionalidad: Consultar)
    return render_template_string(HTML_TEMPLATE, registros=registros)

@app.route('/agregar', methods=['POST'])
def agregar():
    # Recibe un dato del formulario y lo guarda (Funcionalidad: Registrar)
    dato = request.form.get('nuevo_dato')
    if dato:
        registros.append(dato)
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)