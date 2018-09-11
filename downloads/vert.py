# This program asks for user input and prints each word on a separate line

user_input = input("Please enter a string: ")

words = user_input.split()

for i in words:
    print(i)

# Another way of doing the same thing is the following:
#
# for i in range(len(words)):
#    print(words[i])
