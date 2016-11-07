from sys import argv # this is called an import, python asks you to say what you plan to use. this keeps your program small but it also acts as documentation for other programmers who read your code later

script, first, second, third = argv # argument variable, this line unpack argv

y = raw_input("Your fourth variable? ")

print "The script is called:", script
print "Your first variable is:", first
print "Your secind variable is:", second
print "Your third variable is:", third
print "Your forth variable is:", y


