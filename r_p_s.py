import random
print("Welcome to the Rock, Paper, Scissor Simulator")

again = True

while again:
    output = random.randint(1, 4)
    game = input("Enter your choice = Rock,Paper or Scissor = (r/p/s) = ")
    if output == 1:
        x = "r"
        if game.lower() == x:
            print("Computer chose Rock as well, game is a draw")
        elif game.lower() == "p":
            print("You win, computer chose rock")
        else:
            print("You lost, computer chose rock")
    elif output == 2:
        y = "p"
        if game.lower() == y:
            print("Computer chose Paper as well, game is a draw")
        elif game.lower() == "r":
            print("You lost, computer chose paper")
        else:
            print("You won, computer chose paper")
    else:
        z = "s"
        if game.lower() == z:
            print("Computer chose Scissor as well, game is a draw")
        elif game.lower() == "p":
            print("You lost, computer chose scissor")
        else:
            print("You won, computer chose scissor")
    replay = input("Would you like to play again (y/n) = ")
    if replay.lower() != "y":
        break
    else:
        continue
