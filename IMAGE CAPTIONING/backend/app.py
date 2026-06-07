from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

from predict import generate_caption

app = Flask(__name__)

CORS(app)     # <-- ADD THIS

@app.route("/")
def home():
    return "Backend Running"

@app.route("/caption", methods=["POST"])
def caption():

    image = request.files["image"]

    image.save("temp.jpg")

    result = generate_caption("temp.jpg")

    return jsonify({
        "caption": result
    })

if __name__ == "__main__":
    app.run(debug=True)