my_name = "Lei Yunhe"
my_age = 28
my_height = 158
my_weight = 52
my_eyes = 'Black'
my_teeth ='White'
my_hair = 'Black'

print ("Let's talk about %s." % my_name)
print ("She's %d centimeters tall." % my_height)
print ("She's %d kilometers heavy." % my_weight)
print ("Actually that's not too light.")
print ("She's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("Her teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight))