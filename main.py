from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor OCR ativo"

@app.route("/api/ocr", methods=["POST"])
def ocr():

    data = request.json
    image_url = data.get("image")

    print("Recebido para OCR:", image_url)

    # MOCK inicial (teste de integração)
    return jsonify({
        "text": "OCR OK",
        "confidence": 99
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
