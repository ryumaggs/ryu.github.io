# This program takes an amount of change from the user, and computes the
# numbers of each coin using the smallest total number of coins possible.

remainder = eval(input("Enter the total amount in cents (<100) "))

quarters = remainder // 25 
remainder = remainder % 25
dimes = remainder // 10 
remainder = remainder % 10
nickels = remainder // 5 
pennies = remainder % 5

print("pennies: ", pennies)
print("nickels: ", nickels)
print("dimes: ", dimes)
print("quarters: ", quarters)
