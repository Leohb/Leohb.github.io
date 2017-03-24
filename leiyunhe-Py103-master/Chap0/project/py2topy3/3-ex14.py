from sys import argv
#import argparse    #python3，use"argparse"

script, user_name = argv
prompt = '>'

# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()

print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions.")

print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s?" % user_name)
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes,lives,computer))