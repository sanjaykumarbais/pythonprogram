import sys

try:
    n = int(input("please enter an integer: "))
except ValueError:
    sys.exit("you have not entered an integer. try again")

if n%2==0:
    print("{} is even.".format(n))
else:
    print("{} is odd.".format(n))
