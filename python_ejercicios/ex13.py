from sys import argv # this is called an import, python asks you to say what you plan to use. this keeps your program small but it also acts as documentation for other programmers who read your code later

script, first, second, third = argv # argument variable, this line unpack argv

print "The script is called:", script
print "Your first variable is:", first
print "Your secind variable is:", second
print "Your third variable is:", third


# these little things you import to make your Python program do more are called modules or libraries (por ejemplo sys)

# si lo corro asi nomas recibo el error

# ValueError: need more than 1 value to unpack

# lo tengo que correr asi:

# python ex13.py primera segunda tercera

# Are the command line arguments strings?
# Yes, they come in as strings, even if you typed numbers on the command line. Use int() to convert them just like with int(raw_input()).
