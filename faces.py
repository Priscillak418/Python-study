def convert(text):
    converted_text = text.replace(":)", "🙂").replace(":(", "🙁")
    return converted_text

def main():
    user_input = input("What's on your mind? ")
    final_result = convert(user_input)
    print(final_result)

main()