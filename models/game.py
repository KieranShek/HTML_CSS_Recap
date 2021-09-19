from models.player import *

class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = ""

    def play_game(self):
        if self.player_1.choice == self.player_2.choice:
                self.winner = None

        elif self.player_1.choice == "rock":
            if self.player_2.choice == "paper":
                self.winner = self.player_2.name
            else:
                self.winner = self.player_1.name
        
        elif self.player_1.choice == "paper":
            if self.player_2.choice == "scissors":
                self.winner = self.player_2.name
            else:
                self.winner = self.player_1.name

        elif self.player_1.choice == "scissors":
            if self.player_2.choice == "rock":
                self.winner = self.player_2.name
            else:
                self.winner = self.player_1.name
