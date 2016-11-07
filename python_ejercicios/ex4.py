name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# find and replace



# %r no discrimina tipo (string, char, float...)
print "hola %r" %"hola"
# hola 'hola'
print "hola %r" %1
# hola 1
print "hola %r" %'hola'
# hola 'hola'
print "hola %.2r" %1
# hola 1
print "hola %.2r" %1.222
# hola 1.
print "hola %.2r" %5.0/2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
print "hola %.2r" %(5.0/2)
# hola 2.
print "hola %.3r" %(5.0/2)
# hola 2.5
print "hola %.3r" %msdngsng
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'msdngsng' is not defined
print "hola %.3r" %"msdngsng"
# hola 'ms
print "hola %.3s" %"msdngsng"
# hola msd
print "hola %.3c" %"msdngsng"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: %c requires int or char
print "hola %.3c" %c
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'c' is not defined
print "hola %.3c" %"c"
# hola c
print "hola %c" %"c"
# hola c


round(4.7777)



