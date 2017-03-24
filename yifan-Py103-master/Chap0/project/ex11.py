#! python3
# raw_input() was renamed to input()
print ("How old are you?", end = ' ')
age = input()
print ("How tall are you?", end = ' ')
height = input()
print ("How much do you weight?", end = ' ')
weight = input()

print ("So, you're %d old, %r tall and %r heavy." % (
int(age), height, weight
))
