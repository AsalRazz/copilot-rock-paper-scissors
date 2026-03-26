from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__, static_folder='static', static_url_path='')

CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

WINNING_MOVES = {
    "rock":     ["scissors", "lizard"],
    "paper":    ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard":   ["paper", "spock"],
    "spock":    ["rock", "scissors"],
}


def play(user_choice):
    """Run game logic and return result dict."""
    computer_choice = random.choice(CHOICES)
    if user_choice == computer_choice:
        result = "tie"
    elif computer_choice in WINNING_MOVES[user_choice]:
        result = "you win"
    else:
        result = "computer wins"
    return {
        "your_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result,
    }


@app.route("/")
def index():
    """Serve the main game page."""
    return render_template("index.html")


@app.route("/<choice>", methods=["POST"])
def play_via_url(choice):
    """POST /<choice> — e.g. POST /rock"""
    choice = choice.lower()
    if choice not in CHOICES:
        return jsonify({"error": f"Invalid choice. Valid options: {CHOICES}"}), 400
    return jsonify(play(choice)), 200


@app.route("/play", methods=["POST"])
def play_via_body():
    """POST /play with JSON body — e.g. {"choice": "rock"}"""
    data = request.get_json(silent=True)
    if not data or "choice" not in data:
        return jsonify({"error": "Request body must be JSON with a 'choice' field."}), 400
    choice = data["choice"].lower()
    if choice not in CHOICES:
        return jsonify({"error": f"Invalid choice. Valid options: {CHOICES}"}), 400
    return jsonify(play(choice)), 200


if __name__ == "__main__":
    app.run(debug=True)
