# create a mapping of state to abbreviation
provincias = {
    'Rio Negro': 'RN',
    'Misiones': 'MI',
    'Chubut': 'CH'
}

# create a basic set of states and some cities in them
ciudades = {
    'RN': 'Bariloche',
    'MI': 'Posadas'
}

# add some more cities
ciudades['CH'] = 'El Bolson'

# print out some cities
print '-' * 10
print "la provincia de RN tiene: ", ciudades['RN']
print "la provincia de MI tiene: ", ciudades['MI']

# print some states
print '-' * 10
print "la abreviacion de Rio Negro es: ", provincias['Rio Negro']
print "la abreviacion de Misiones es: ", provincias['Misiones']

# do it by using the state then cities dict
print '-' * 10
print "la provincia de Rio Negro tiene: ", ciudades[provincias['Rio Negro']]
print "la provincia de Misiones tiene: ", ciudades[provincias['Misiones']]
print "la provincia de Chubut tiene: ", ciudades[provincias['Chubut']]

# print every state abbreviation
print '-' * 10
for prov, abrev in provincias.items():
    print "%s se abrevia %s" % (prov, abrev)

# print every city in state
print '-' * 10
for abrev, ciud in ciudades.items():
    print "%s tiene la ciudad %s" % (abrev, ciud)

# now do both at the same time
print '-' * 10
for prov, abrev in provincias.items():
    print "La provincia %s se abrovia %s y tiene la ciudad %s" % (
        prov, abrev, ciudades[abrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
provincia = provincias.get('Santiago')

if not provincia:
    print "Perdon, no existe Santiago."

# get a city with a default value
ciudad = ciudades.get('Santiago','no existe')
print "La ciudad para el estado SA es: %s" % ciudad
