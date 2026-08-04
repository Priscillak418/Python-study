def main():
    amount_due = 50
    # print("Amount Due:", amount_due)
    # coin = int(input("Insert coin: "))

    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = int(input("Insert coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount_due = amount_due - coin
    print("Change Owed:", abs(amount_due))

    # while amount_due != 0:
    # if coin == 25:
    #     amount_due = amount_due - coin
    #     print("Amount Due:", amount_due)
    # elif coin == 10:
    #     amount_due = amount_due - coin
    #     print("Amount Due:", amount_due)
    # elif coin == 5:
    #     amount_due = amount_due - coin
    #     print("Amount Due:", amount_due)
    # else:
    #     coin = int(input("Insert coin: "))

    # if amount_due == 0:
    #     print("Change Owed", amount_due)

    # change_owed = amount_due - coin

    # while change_owed != 0:
    #     if coin == 25:
    #         change_owed = amount_due - 25
    #     elif coin == 10:
    #         change_owed = amount_due - 10
    #     elif coin == 5:
    #         change_owed = amount_due - 5
    #     else:
    #         coin = int(input("Insert coin: "))

    # print("Change Owed:", change_owed)


main()


# def main():
#     amount_due = 50
#     print("Amount Due:",amount_due)
#     coin = check_coin(int(input("Insert coin: ")))


# def check_coin(coin):
#     amount_due = 50
#     amount_owed = amount_due - coin


# main()
