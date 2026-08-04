WORDS = {"PAIR": 4, "CHAIR": 5, "HAIR": 4, "GRAPHIC": 7}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        guess = input("Guess the word: ")

        if guess =="GRAPHIC":
            WORDS.clear()
            print("You have won!")
        elif guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"You have {points} points")
    print("That's the game!")       

main()
