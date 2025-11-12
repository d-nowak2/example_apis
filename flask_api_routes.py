# minimal_api.py
from flask import Flask, jsonify, request
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")  # e.g., /?name=David
    message = f"Hello, {name}!" if name else "Hello, World!"
    return jsonify(message=message)

@app.route("/birthyear")
def birthyear():
    name = request.args.get("name")
    age = request.args.get("age", type=int)  # e.g., /birthyear?name=David&age=35

    if not name or age is None:
        return jsonify(error="Please provide both 'name' and 'age' query parameters."), 400
    if age < 0 or age > 150:
        return jsonify(error="'age' must be between 0 and 150."), 400

    current_year = date.today().year
    yob = current_year - age
    return jsonify(name=name, year_of_birth=yob)

if __name__ == "__main__":
    app.run()