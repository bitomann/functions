# Write a program that prints the numbers from 1 to 100. You can use Python's range() to 
# quickly make a list of numbers.
for i in range(1, 101):
    # print(i)

#   For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number.
    if i % 5 == 0:
        print(f"Chicken")

#   For the multiples of seven (7, 14, 21, etc.) print "Monkey".
    elif i % 7 == 0:
        print(f"Monkey")
    

#   For is which are multiples of both five and seven print "ChickenMonkey".
    elif i % 7 == 0 and i % 5 == 0:
        print(f"ChickenMonkey")

# To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator.
    else:
        print(i)