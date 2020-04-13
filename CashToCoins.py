
import math

def calc_coins():
    piggyBank = {
        "quarters": 0,
        "dimes": 0,
        "nickels": 0,
        "pennies": 0
    }

    dollarAmount = 8.69

    piggyBank["quarters"] = math.floor(dollarAmount / 25)
    dollarAmount = piggyBank["quarters"] * 25

    piggyBank["dimes"] = math.floor(dollarAmount / 10)
    dollarAmount = piggyBank["dimes"] * 10

    piggyBank["nickels"] = math.floor(dollarAmount / 5)
    dollarAmount = piggyBank["nickels"] * 5

    piggyBank["pennies"] = math.floor(dollarAmount)

    calc_coins()
print()

