days = 'Mon Tue Wed'
months = 'Jan\nFeb\nMar'

# el \n hace un enter

print 'Here are the days: ', days
print 'Here are the months', months

print """
There's something
in the kitchen.
"""

print '''
There's something
in the kitchen.
'''

# las dos formas funcionan

print 'Here are the days: %r' % days
#Here are the days: 'mon tue wed'
print 'Here are the days: %s' % days
#Here are the days: mon tue wed

days = 'mon\ntue\nwed'
print 'Here are the days: %s' % days
#Here are the days: mon
#tue
#wed
print 'Here are the days: %r' % days
#Here are the days: 'mon\ntue\nwed'

# Why do the \n newlines not work when I use %r?
# That's how %r formatting works; it prints it the way you wrote it (or close to it). It's the "raw" format for debugging.

