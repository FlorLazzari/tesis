class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

ChildA()
ChildB()

# ahora le agrego un atributo "hola" a la clase Base

class Base(object):
    def __init__(self,hola):
        print "Base created"
        self.hola = hola

class ChildA(Base):
    def __init__(self,hola):
        Base.__init__(self,hola)

ChildA(1)


# no estoy entendiendo bien lo que hace super, a partir de aca esta mal:

class ChildB(Base):
    def __init__(self,hola):
        super(ChildB, self).__init__(self.hola)

ChildB(1)


# otra pregunta colgada, de donde vienen los archivos pyc? quien los invito?
# no me caen bien, los puedo borrar sin costo alguno?
