from flask import flask, request
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/calc", methods = ['POST'])
def calculate():
    if request.method == 'POST':
        records = json.loads(request.data)
        num1 = records["number1"]
        num2 = records["number2"]

        addition = int(num1) + int(num2)
        multiplication = int(num1) * int(num2)

        return jsonify({
            'numbers': number1 + " and " + number2,
            'addition': addition,
            'multiplication': multiplication
        })


if __name__ == "__main__":
    app.run()