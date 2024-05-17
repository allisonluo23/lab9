#NAME: Allison Luo
# lab_9a.py
# URL to public GitHub repo: https://github.com/allisonluo23/lab9

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

# Functions
import random

choices = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(choices)

def get_winner(player1, player2):
    if player1 == player2:
        return "Tie"
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'scissors' and player2 == 'paper') or \
         (player1 == 'paper' and player2 == 'rock'):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

def play_once(p1, p2):
    print(f'Player 1 chose: {p1}')
    print(f'Player 2 (Computer) chose: {p2}')
    result = get_winner(p1, p2)
    print(result)
    return result

def play_game(num_players, rounds):
    if num_players == 0:
        player1 = get_computer_choice()
        player2 = get_computer_choice()
    elif num_players == 1:
        player1 = input('Player 1, pick one of rock, paper, or scissors: ')
        player2 = get_computer_choice()
    else:
        player1 = input('Player 1, pick one of rock, paper, or scissors: ')
        player2 = input('Player 2, pick one of rock, paper, or scissors: ')

    results = {"Player 1 wins": 0, "Player 2 wins": 0, "Tie": 0}
    for _ in range(rounds):
        result = play_once(player1, player2)
        results[result] += 1

    print(f'\nResults after {rounds} rounds:')
    print(f"Player 1 wins: {results['Player 1 wins']}")
    print(f"Player 2 wins: {results['Player 2 wins']}")
    print(f"Ties: {results['Tie']}")

# Example usage
num_players = int(input('Enter number of players (0, 1, or 2): '))
rounds = int(input('Enter number of rounds: '))
play_game(num_players, rounds)


# Classes
import random

choices = ['rock', 'paper', 'scissors']

class RockPaperScissors:
    def __init__(self):
        self.results = {"Player 1 wins": 0, "Player 2 wins": 0, "Tie": 0}
    
    def get_computer_choice(self):
        return random.choice(choices)
    
    def get_winner(self, player1, player2):
        if player1 == player2:
            return "Tie"
        elif (player1 == 'rock' and player2 == 'scissors') or \
             (player1 == 'scissors' and player2 == 'paper') or \
             (player1 == 'paper' and player2 == 'rock'):
            return "Player 1 wins"
        else:
            return "Player 2 wins"
    
    def play_once(self, p1, p2):
        print(f'Player 1 chose: {p1}')
        print(f'Player 2 chose: {p2}')
        result = self.get_winner(p1, p2)
        print(result)
        self.results[result] += 1
    
    def play_game(self, num_players, rounds):
        for _ in range(rounds):
            if num_players == 0:
                player1 = self.get_computer_choice()
                player2 = self.get_computer_choice()
            elif num_players == 1:
                player1 = input('Player 1, pick one of rock, paper, or scissors: ')
                player2 = self.get_computer_choice()
            else:
                player1 = input('Player 1, pick one of rock, paper, or scissors: ')
                player2 = input('Player 2, pick one of rock, paper, or scissors: ')
            
            self.play_once(player1, player2)
        
        print(f'\nResults after {rounds} rounds:')
        print(f"Player 1 wins: {self.results['Player 1 wins']}")
        print(f"Player 2 wins: {self.results['Player 2 wins']}")
        print(f"Ties: {self.results['Tie']}")

# Example usage
game = RockPaperScissors()
num_players = int(input('Enter number of players (0, 1, or 2): '))
rounds = int(input('Enter number of rounds: '))
game.play_game(num_players, rounds)
