# for number in range(1,10,2):
#     print("Attempt", number, number * ".")

#Nested loops
sizes = ["Small", "Large"]
flavors = ["Vanilla", "Chocolate", "Strawberry"]

for size in sizes:
    print(f"-----Creating {size} cones----")
    for flavor in flavors:
        print(f"{size} {flavor}")