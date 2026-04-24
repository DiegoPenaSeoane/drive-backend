from flask import Flask, request, send_from_directory, jsonify
import os

app = Flask(__name__)

# Carpeta para almacenar archivos
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Backend activo. Usa /files para ver los archivos."

# Listar archivos
@app.route("/files", methods=["GET"])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files)

# Subir archivo
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No se encontró archivo", 400
    file = request.files["file"]
    if file.filename == "":
        return "Archivo sin nombre", 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return f"Archivo {file.filename} subido exitosamente", 200

# Descargar archivo
@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)