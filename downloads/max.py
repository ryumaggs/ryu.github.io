# This program asks the user for 3 values and prints the maximum of them
# Note that we are assuming three distinct values

x1 = eval(input("Please enter a number: "))
x2 = eval(input("Please enter a number: "))
x3 = eval(input("Please enter a number: "))

if x1 > x2 and x1 > x3 :
    maximum = x1
elif x2 > x1 and x2 > x3 :
    maximum = x2
else :
    maximum = x3

print("The maximum of " + str(x1) + ", ", end="")
print(str(x2)+ ", and " + str(x3) + " is", maximum)


## There is always another way to do the same thing:
##
## y = []
## for i in range(3):
##    y = y + [eval(input("Please enter a number: "))]
##
## maximum = y[0]
## for i in range(1,len(y)):
##    if y[i] > maximum:
##        maximum = y[i]
##
## print("The maximum of " + str(y[0]) + ", ", end="")
## print(str(y[1])+ ", and " + str(y[2]) + " is", maximum)
