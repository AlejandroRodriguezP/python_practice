'''
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
'''

def play_again():
    wanna_play = input("You wanna play again? (yes / no) ")
    if wanna_play == "yes":
        print("alright, lets play")
        start_game()
    elif wanna_play == "no":
        print("aright,see you soon.")
        start_game()
    else: print("thats not a valid input")
    play_again()

def start_game():
# Variables
 player1_moves = input("PLAYER 1: please enter a move (ex: rock, paper or scissors) ")
 player2_moves = input("PLAYER 2: please enter a move (ex: rock, paper or scissors) ")

# Logic
 while player1_moves == "rock":
    if player2_moves == "rock":
        print("TIE ")
        break
    elif player2_moves == "paper":
        print("Player 2 wins, paper beats rock ")
        break
    elif player2_moves == "scissors":
        print("Player 1 wins, rock beats scissors")
        break
    else:
        print("INVALID MOVE")
        break

 while player1_moves == "paper":
    if player2_moves == "rock":
        print("Player 1 wins, paper beats rock ")
        break
    elif player2_moves == "paper":
        print("TIE")
        break
    elif player2_moves == "scissors":
        print("Player 2 wins, scissors beat paper...duh!")
        break
    else:
        print("INVALID MOVE")
        break

 while player1_moves == "scissors":
    if player2_moves == "rock":
        print("Player 2 wins, rock beats paper")
        break
    elif player2_moves == "paper":
        print("Player 1 wins, scissors beat paper...duh!")
        break
    elif player2_moves == "scissors":
        print("TIE")
        break
    else:
        print("INVALID MOVE")
        break


start_game()
