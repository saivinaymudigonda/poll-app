from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

poll = {
    "question": "Your favorite language?",
    "options": [
        {"text": "Python", "votes": 0},
        {"text": "Java", "votes": 0}
    ]
}

@app.route("/poll", methods=["GET"])
def get_poll():
    return jsonify(poll)

@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    poll["options"][data["option"]]["votes"] += 1
    return jsonify(poll)

app.run(debug=True)