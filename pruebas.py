
#cadenas de texto
my_hello_world = "Hello World!"
print(my_hello_world)
#valores numericos
number = 43.5
number2 = 24

print(number+number2)

#diccionarios

my_dict = dict()

#declaracion con asignacion de valor a la llave
my_dict['llave_1'] = "valor_1"
# adicion de llaves con el metodo update

my_dict.update({'llave_2': 'valor_2'})

print(my_dict) #impresion rapida

#iteracion tradicional en dictionarios

for k,v in my_dict.items():
	print("la llave es " + k + " y el valor es " + v)

#Funciones basicas
def sumaValores(a,b):
	'''Funcion para sumar    '''
	return a+b

print(sumaValores(45,72) )

#ejercicios de repaso

def calculoDeAreaDeUnTriangulo(base,altura):
	'''Definir el calculo del area a partir de su base y altura'''
	#codigo aca, retornar valor
	pass

print(calculoDeAreaDeUnTriangulo(4,5)  ) #debe retornar 10

def factorial(valor):	
	'''Definir la funcion recursiva del calculo factorial'''
	pass

print(factorial(8))  #debe imprimir 40320

def palindromo(cadena_de_texto):
	'''Definir una funcion que verifica si una cadena de texto es palinfromo'''

	pass

print(palindromo('anitalavalatina') )   #debe retornar verdadero

def separar_palabras(texto):
	''' Se debe separa cada palabra de un texto e imprimir una lista 
	para cada palabra, las palabras seran separadas por un espacio'''
	#codigo de la funcion
	pass 

separar_palabras('Si se puede imaginar, se puede programar')



def identificar_valores_altos(lista, metrica):
	'''Dada una funcion de verificacion, iterar sobre una lista y retornar
	los elemetos de la lista que cumplan con la verificacion '''
	# lista_nueva = list()
	# iteracion
		# condicion a cumplir de la verificacion con el valor mayor a de la metrica
			# añadir valor a la nueva lista
	#retornar nueva lista
	pass

def regla_de_verificacion(valor,metrica):
	'''si el valor a es mayor al valor b retornar verdadero '''
	pass


lista= [44,75,98,36,0,21,-12,63,44]

n_lista = identificar_valores_altos(lista, 50 )

print(n_lista)



