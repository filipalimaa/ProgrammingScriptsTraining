from flask import Flask, render_template, request, redirect, session
import secrets
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Rota para exibir o formulário de login
@app.route('/')
def index():
    # Gera e armazena um token anti-CSRF na sessão
    if 'csrf_token' not in session:
        session['csrf_token'] = os.urandom(24).hex()
    return render_template('login.html', csrf_token=session['csrf_token'])

# Rota para processar o formulário de login
@app.route('/login', methods=['POST'])
def login():
    # Verifica se o token anti-CSRF é válido
    if request.form.get('csrf_token') != session.pop('csrf_token', None):
        return 'Token CSRF inválido', 403
    # Processa a autenticação
    username = request.form.get('username')
    password = request.form.get('password')
    # Aqui faria a autenticação real, por exemplo, verificar em um banco de dados
    # Aqui, apenas para fins de exemplo, verificamos se o utilziador é "admin" e a senha é "senha"
    if username == 'admin' and password == 'senha':
        return 'Login bem-sucedido'
    else:
        return 'Utilizador ou senha inválidos', 401

if __name__ == '__main__':
    app.run(debug=True)


