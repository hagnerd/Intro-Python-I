# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(n):
    """ checks if a number is even """
    return n % 2 == 0

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def alt_is_even(n):
    """ uses is_even to determine whether it should print Even or Odd """
    if is_even(n):
        print("Even!")
    else:
        print("Odd")

alt_is_even(num)
