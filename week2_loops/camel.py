def main():
    name = input("camelCase: ")

    print("snake_case: ", end="")

    for x in name:
        if x.isupper():
            print("_" + x.lower(), end="")
        else:
            print(x, end="")

    print()


main()
