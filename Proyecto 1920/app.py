from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "clave_super_secreta"

# Almacenamiento en memoria por ahora (puedes conectar a Supabase después)
usuarios = {}
frases = []

@app.route('/')
def index():
    return render_template("index.html", frases=frases)

@app.route('/publicar', methods=['POST'])
def publicar():
    texto = request.form['texto']
    autor = session.get("usuario", "Anónimo")
    frases.append({
        "autor": autor,
        "texto": texto,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    nombre = request.form['usuario']
    session['usuario'] = nombre
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run()
