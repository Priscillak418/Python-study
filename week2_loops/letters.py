# Princess peach is writing letters to invite people

def main():
    names = ["Mary", "George", "Tom"]
    for name in names:
        print(write_letters(name, "Princess Peach"))


def write_letters(receiver, sender):
    return f"{receiver} is invited to the ball, yours truly, {sender}"


main()
