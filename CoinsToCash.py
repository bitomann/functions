# Create a function that will take all your coins and convert 
# it to the cash amount.

def calc_dollars(**coins):
    # The function should look at each key (pennies, nickels, 
    # dimes and quarters) and perform the appropriate math on 
    # the integer value to determine how much money you have 
    # in dollars. Store that value in a variable named 
    # `dollarAmount` and print it.

    dollarAmount = 0
    # '\' allows code to go to the next line with out spacing issues  vvv
    dollarAmount = (coins["pennies"] * .01) + (coins["nickels"] * .05) + \
         (coins["dimes"] * .10) + (coins["quarters"] * .25)
    print(f"There is ${dollarAmount} in my account! ")

calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)