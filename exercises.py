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




