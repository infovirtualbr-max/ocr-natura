from flask import Flask, request, jsonify
import pytesseract
import requests
import tempfile
from pdf2image import convert_from_bytes

app = Flask(__name__)

@app.route("/")
def home():
    return "VERSAO NOVA"

@app.route("/api/ocr", methods=["POST"])
def ocr():

    data = request.json
    pdf_url = data.get("image")

    print("Processando:", pdf_url)

    r = requests.get(pdf_url)
    images = convert_from_bytes(r.content)

    texto_final = ""

    for img in images:
        texto_final += pytesseract.image_to_string(img, lang="por")

    return "VERSAO NOVA"({
        "text": texto_final,
        "confidence": 90
    })


