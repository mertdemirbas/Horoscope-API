from flask import Flask, jsonify, request
from flask_cors import CORS
from pyhoroscope import get_today_horoscope

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Horoscope API çalışıyor."

@app.route("/horoscope/today/<sign>", methods=["GET"])
def today_horoscope(sign):
    result = get_today_horoscope(sign.lower())
    return jsonify(result)

# Sunucuyu dış dünyaya aç
import os
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
