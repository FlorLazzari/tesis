from sys import argv

script, user_name = argv
prompt = '> '
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name

likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
So you said %r about liking me.
You live in %r.
And you have a %r computer
""" % (likes, lives, computer)

# ojo! "script" ya es una palabra para python, pero "user_name" no

