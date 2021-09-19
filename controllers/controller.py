from flask import render_template, request, redirect
from app import app
from models.game import *
from models.player import *
import random

@app.route("/home")
def home():
    return render_template("home.html", title = "Home")

@app.route("/")
def welcome():
    return render_template("welcome.html", title = "Welcome")

@app.route('/play', methods=["GET", "POST"])
def get_choices():
        # player_1 = Player(request.form["Player 1 Name"], request.form["Player 1 Choice"])
        # player_2 = Player(request.form["Player 2 Name"], request.form["Player 2 Choice"])
        choice_1 = request.form["Player 1 Choice"]
        choice_2 = request.form["Player 2 Choice"]
        player_1 = request.form["Player 1 Name"]
        player_2 = request.form["Player 2 Name"]
        if player_2 == "CPU" and choice_2 == "":
            choice_2 = random.choice(["rock", "paper", "scissors"])
        return redirect(str("/" + player_1 + "/" + choice_1 + "/" + player_2 + "/" + choice_2))

@app.route("/<name_1>/<choice_1>/<name_2>/<choice_2>")
def play(name_1, choice_1, name_2, choice_2):
    player_1 = Player(name_1, choice_1)
    player_2 = Player(name_2, choice_2)
    game = Game(player_1, player_2)
    game.play_game()
    winner = game.winner
    return render_template("result.html", title = "Results", winner = winner, name_1 = name_1, name_2 = name_2, choice_1 = choice_1, choice_2 = choice_2)
