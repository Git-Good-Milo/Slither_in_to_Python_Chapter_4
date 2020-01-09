# Question 1
# Write a program that takes three inputs, a, b and c and prints out whether or not those numbers form a right angled triangle. The formula you'll need is c**2 = (a**2) + (b**2)

# First we must set the variables for a, b and c
a = int(input("Select a number for a: "))
b = int(input("Select a number for b: "))
c = int(input("Select a number for c: "))

# Then we need to construct the if script to determine if the numbers form a right angle
if c == (a**2 + b**2)**0.5:
    print(f"Your number {c} for c forms a right angle with a and b")
else:
    print(f"Sorry! Your number {c} for c does not form a right angled triangle with a and b")

# Question 2
# Fizz buzz is a game in which the following rules apply:
    # any number which is divisible by 3 is replaced with fizz
    # any number which is divisible by 5 is replaced with buzz
    # any number which is divisible by both 3 and 5 is replaced with fizz-buzz
    # any other number is just the number itself

# First we assign a variable with an input
number = int(input("Please select a number for Fizbuzz: "))

# Then we create an if statement to satisfy the least likely senario

if number %5 == 0 and number %3 == 0:
    print("FIZBUZ!!!")
elif number %5 == 0:
    print("BUZZ!!!")
elif number % 3 == 0:
    print("FIZ!!!")

else:
    print("Sorry your number is invalid")

# Question 3
# Write a program which takes in six numbers, x1, y1, r1 and x2, y2, r2 (which are the x and y coordinates of the center of a circle and that circles radius) and print out whether or not the two circles overlap.

# First we set the variables to a user input for the first circle
x1 = int(input("Please enter an x1 value: "))
y1 = int(input("Please enter a y1 value: "))
r1 = int(input("Please select an r1 value: "))

# we repeat this process for the second circle
x2 = int(input("Please enter an x2 value: "))
y2 = int(input("Please enter a y2 value: "))
r2 = int(input("Please select an r2 value: "))

# Next we need to write out an if statement to see if the input values cause the circles to overlap
circle_overlap =
