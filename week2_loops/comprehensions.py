#   A concise way to create lists in python
#   Its compact and easier to read than traditional loops
#   [Expression for value in iterable if condition]

# doubles = [x*2 for x in range(1, 11)]
# triples = [y*3 for y in range(1,11)]

# print(triples)

numbers = [1, -2, 3, -4, 5, -6]

positive_nums = [number for number in numbers if number >= 0]
negative_nums = [number for number in numbers if number < 0]

print(negative_nums)
