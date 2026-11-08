#metodo

# tipo de escritura:(
#   class (nombre de la clase)
#       def(nombre del metodo) (SELF):
#   self. (nombre de la variable ) = (algoritmo) 
# 
# )


class Matematicas:
    #self = para crear atributos asi mismo (objeto)
    def suma(self):
        #atributos
        self.n1 = 2
        self.n2 = 3

# s = objeto
s = Matematicas()
s.suma()
#metodo
print(s.n1 + s.n2)



#metodo 2
# (constructor ) _init_(SEFT) = iniciar 



class Calculadora:
    def __init__(self,m1,m2):
        self.sma = m1 + m2
        self.resta = m1 - m2
        self.producto = m1 * m2
        self.division = m1 / m2

a=int(input("primer numero "))
b=int(input("Segundo numero "))

#operacion = objneto
operacion = Calculadora(a,b)
print(operacion.sma)

#funciones para atributos: (
#   getattr : traer atributo
#   hasattr : true, false
#   setattr : ingreso de otro valor
#   delattr : eliminar atributos 
#
# todo se escribe tal cual "print( "", funcion(objeto,'atributo'))"
#)


#constructor: ( __init__()
#   se usa para inicializar todo tipo de variable
#
#
#
#)

class persona:
    pass 

    #construcctor
    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año

    #metodo
    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre,self.año)

    #otro metodo
    def comentario(self, frase):
        return ' {} dice: {}'.format(self.nombre,frase)

doctor  = persona('jose',26)
print(doctor.descripcion())
print(doctor.comentario('hola, que tal?'))

#otro ejemplo
class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()

print(mi_correo.enviado)

mi_correo.enviar_correo()
print(mi_correo.enviado)


# herencia 
#   class NombreSubClase (nombreClaseSuperior)
#
#   class ClaseBase:
#       Cuerpo de la clase base
#   
#   class DerivadoCLase (ClaseBase):
#       Cuerpo de clase derivada


class pokemon:
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre,self.tipo)
class pikachu (pokemon):
    def ataque(self,tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)
class charmander(pokemon):
    def ataque(self,tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)

nuevo_pokemon = pikachu('boby','electrico')
print(nuevo_pokemon.descripcion())