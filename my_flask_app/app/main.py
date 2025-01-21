from flask import Flask

app = Flask(__name__)  # Instância da aplicação Flask

@app.route("/")  # Rota principal da aplicação
def home():
    returrn "<h1>Hello, NTT DATA</h1>"  # Retorna uma resposta HTML para o navegador

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Executa o servidor