
from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/', methods=["POST"])  # home.html
def home_page():
    return render_template("home.html")


@app.route('/results', methods=["POST"])
def results():
    choices = ["Rock", "Paper", "Scissors"]
    res = ""
    user_choice = ""
    comp_choice = random.choice(choices)
    if request.form.get("rock"):
        user_choice = "Rock"
        if comp_choice == "Rock":
            res = "You Tied"
        elif comp_choice == "Scissors":
            res = "You Won"
        elif comp_choice == "Paper":
            res = "You Lost"

    elif request.form.get("scissors"):
        user_choice = "Scissors"
        if comp_choice == "Rock":
            res = "You Lost"
        elif comp_choice == "Scissors":
            res = "You Tied"
        elif comp_choice == "Paper":
            res = "You Won"

    elif request.form.get("paper"):
        user_choice = "Paper"
        if comp_choice == "Rock":
            res = "You Won"
        elif comp_choice == "Scissors":
            res = "You Lost"
        elif comp_choice == "Paper":
            res = "You Tied"

    return render_template("results.html", comp_choice=comp_choice, user_choice=user_choice, res=res)


if __name__ == "__main__":
    app.run(debug=True)


