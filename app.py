from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend funcionando 🚀"

@app.route("/saludo")
def saludo():
    return {"mensaje": "Hola desde Railway 🚀"}

@app.route("/suma")
def suma():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return {"resultado": a + b}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)