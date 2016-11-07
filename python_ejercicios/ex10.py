"I am 6'2\" tall."  # escape double-quote inside string
'I am 6\'2" tall.'  # escape single-quote inside string

tabby = "\tI'm tabbed."
persian = "I'm split\non a line."
backslash = "I'm \\ a \\ cat."

fat = """
I'll do a list:
\t* cat food
\t* fich
\t* green\n\t* grass
"""

print tabby
print persian
print backslash
print fat

while True: # esto es una forma cabeza de escribir un loop infinito
    for i in ["/","-","|","\\","|"]:   # esto es una lista, lo que esta entre parentesis es una tupla
        print "%s\r" % i, # \r = Carriage Return (CR)
