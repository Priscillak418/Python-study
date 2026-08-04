def main():
    text = input("Input: ")
    new_text = ""

    for x in text:
        if x.lower() not in "aeiou":
            new_text = new_text + x

    print("Output:", new_text)


main()
