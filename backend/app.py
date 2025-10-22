from flask import Flask
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


@app.route("/random-color")
def random_color():
    hex_code = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
    ]
    random_hex_code = "#"
    for _ in range(6):
        random_hex_code += random.choice(hex_code)
    return {"random_color": random_hex_code.upper()}


if __name__ == "__main__":
    app.run()
