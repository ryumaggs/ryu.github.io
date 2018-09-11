# The program takes the users input for a base and power, and
# gives the result of base^power

base = eval(input("Please enter the base "))
power = eval(input("Please enter the power "))

result = 1
for i in range(power):
    result = result * base

print("The result of ", base, " raised to the power of ", power, " is ", result)

