# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir requisições de outro domínio (como localhost:5500)

@app.route("/api", methods=["POST"])
def responder():
    dados = request.get_json() # Ler os dados recebidos (json)
    nome = dados.get("nome", "desconhecido") # obter os dados
    return jsonify({"mensagem": f"Olá, {nome}! A tua mensagem foi recebida com AJAX."})

if __name__ == "__main__":
    app.run(debug=True)
