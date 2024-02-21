import json
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/upload", methods=["GET"])
def upload():
    img_url = request.args.get("image_url")
    print(img_url)
    return f"Hellon{img_url}"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
