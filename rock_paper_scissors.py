'''
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
'''


def play_again():
    # Variables
    wanna_play = input("You wanna play again? (yes / no) ")

    # Logic
    if wanna_play == "yes":
        print("alright, lets play")
        start_game()
    elif wanna_play == "no":
        print("aright,see you soon.")
        return False
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
        play_again()
        break
    elif player2_moves == "paper":
        print("Player 2 wins, paper beats rock ")
        play_again()
        break
    elif player2_moves == "scissors":
        print("Player 1 wins, rock beats scissors")
        play_again()
        break
    else:
        print("INVALID MOVE")
        play_again()
        break

 while player1_moves == "paper":
    if player2_moves == "rock":
        print("Player 1 wins, paper beats rock ")
        play_again()
        break
    elif player2_moves == "paper":
        print("TIE")
        play_again()
        break
    elif player2_moves == "scissors":
        print("Player 2 wins, scissors beat paper...duh!")
        play_again()
        break
    else:
        print("INVALID MOVE")
        play_again()
        break

 while player1_moves == "scissors":
    if player2_moves == "rock":
        print("Player 2 wins, rock beats paper")
        play_again()
        break
    elif player2_moves == "paper":
        print("Player 1 wins, scissors beat paper...duh!")
        play_again()
        break
    elif player2_moves == "scissors":
        print("TIE")
        play_again()
        break
    else:
        print("INVALID MOVE")
        play_again()
        break


start_game()
