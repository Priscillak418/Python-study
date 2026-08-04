def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False

    seen_number = False
    for char in s:
        if char.isdigit():
            if char == "0" and seen_number == False:
                return False
        
            seen_number = True

        elif char.isalpha():
            if seen_number == True:
                return False
    
    
    return True


main()
