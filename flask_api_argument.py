# minimal_api.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")  # /?name=David
    message = f"Hello, {name}!" if name else "Hello, World!"
    return jsonify(message=message)

if __name__ == "__main__":
    app.run()