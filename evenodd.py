import sys

try:
    n = int(input("Please enter an integer: "))
except ValueError:
    sys.exit("You have not entered an integer. Try again")

if n%2==0:
    print("{} is even.".format(n))
else:
    print("{} is odd.".format(n))
