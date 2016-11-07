formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) # es una tupla de char
print formatter % ("one", "two", "three", "four") # es una tupla de strings 

print formatter % (True, False, False, True) # es una tupla de argumentos binarios?

print formatter % (formatter, formatter, formatter, formatter) # es una tupla de ??

print formatter % (
    "little",
    "lamb",
    "super",
    "power"
) 

print formatter % (
    "little",
    "lamb",
    "super",
    "power") # y si cambio el parentesis?

# ahora cambio el %r por lo que es el formato   

print "cambio el %r !!"

formatter = "%c %c %c %c"

print formatter % (1, 2, 3, 4) # es una tupla de char

formatter = "%f %f %f %f"

print formatter % (1, 2, 3, 4) # es una tupla de char

formatter = "%s %s %s %s"

print formatter % ("one", "two", "three", "four") # es una tupla de strings 

# cambia la forma de printearla?

# formatter = "%a %a %a %a"

#                 unsupported format character 'a' ??

#                 print formatter % (True, False, False, True) # es una tupla de argumentos binarios?

# formatter = "% % % %"  # que pongo aca si no es el r ??

# print formatter % (formatter, formatter, formatter, formatter) # es una tupla de ??

formatter = "%s %s %s %s"

print formatter % (
    "little",
    "lamb",
    "super",
    "power"
) 

# You should use %s and only use %r for getting debugging information about something. The %r will give you the "raw programmer's" version of variable, also known as the "representation."

# Python is going to print the strings in the most efficient way it can, not replicate exactly the way you wrote them. This is perfectly fine since %r is used for debugging and inspection, so it's not necessary that it be pretty.

# Debugging is the process of finding and resolving of defects that prevent correct operation of computer software or a system. 
