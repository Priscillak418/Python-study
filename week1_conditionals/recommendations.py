# A program that recommends games to user according to the level of difficulty or number of players

def main():
    difficulty = input("Enter difficulty (Difficult or Casual): ")
    if not(difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter valid difficulty")
        return

    player = input("Enter player (Single-player or Multi-player): ")
    if not(player =="Single-player" or player =="Multi-player"):
        print("Enter valid player")
        return

    if difficulty == "Difficult" and player == "Single-player":
        recommend("Minesweeper")
    elif difficulty == "Difficult" and player == "Multi-player":
        recommend("Poker")
    elif difficulty == "Casual" and player == "Single-player":
        recommend("Candy Crush")
    else:
        recommend("Ludo")


def recommend(game):
    print(f"You might like {game}")


main()
