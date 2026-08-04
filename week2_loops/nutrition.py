def main():
    fruit_collection = {"apple": "130",
                        "avocado": "50",
                        "sweet cherries": "100"}
    
    fruit = input("Item: ").lower()

    if fruit in fruit_collection:
        print(f"Calories: {fruit_collection[fruit]}")


main()
