# print("Meow\n" * 3, end="")

# for _ in range(8):
#     print("Meow")

# While
# i = 1

# while i < 5:
#     print(i)
#     i += 1


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is n? "))
        if n>0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("Meow")
