#################LISTAS####################
###########################################
# Función: Declaración de Lista. Estructura de datos dinámica y mutable.
# Almacena elementos en un orden secuencial (indexado).
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
#input()
print(my_lista)

# Función: type() verifica qué clase de objeto es la variable (devuelve <class 'list'>).
print(type(my_lista))
# Función: Acceso directo. Busca el elemento en el índice 2 (las listas empiezan en 0).
print(my_lista[2])

# Función: len() calcula la longitud total (cantidad de elementos) de la estructura.
print("my_lista size: ", len(my_lista))

# Función: Slicing (Rebanado). Extrae una sublista desde el índice 0 hasta el 2 (sin incluir el 2).
print(my_lista[0:2])
# Función: Slicing implícito. Si omites el primer número, asume que arranca desde el índice 0.
print(my_lista[:2])

# Función: .append() inserta un único elemento al final de la lista.
my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista)

# Función: .insert(índice, valor) coloca un elemento en una posición exacta.
# Empuja los elementos siguientes un índice hacia la derecha.
my_lista.insert(3, 'Negro')
print(my_lista)

# Función: .extend() desempaqueta la lista dada y concatena sus elementos al final de la lista actual.
# (A diferencia de append, que metería la lista entera como un solo elemento).
my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)

# Función: .index() busca un valor de izquierda a derecha y retorna su posición (índice).
print(my_lista.index('Azul'))

#my_lista.remove('Magenta') # Función: Da un ValueError porque 'Magenta' no existe.
# Función: .remove() busca el valor y elimina su primera coincidencia en la lista.
my_lista.remove('Marron')
print(my_lista)

my_lista.insert(8, 'Marron')
print(my_lista)

# Función: .pop() extrae y elimina el ÚLTIMO elemento de la lista si no se le pasan argumentos.
# Retorna el valor extraído (en este caso imprimirá 'Gris').
print(my_lista.pop())
size = len(my_lista)
print("size = ", size)
#print(my_lista.pop(size)) # Función: Da IndexError. El índice máximo es size-1.

# Función: Repetición. El operador '*' duplica el contenido de la lista secuencialmente.
my_lista_3 = my_lista*3
print("my_lista_3: ", my_lista_3)

print("Sort:")
print()
# .sort() ordena la lista original "in-place" y devuelve 'None'.
# my_listaSort guardará 'None', no la lista ordenada.
my_listaSort = my_lista.sort()
print(my_listaSort) # Esto imprimirá None

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
# Función: .sort() aplicado correctamente. Ordena directamente my_NumList en memoria (ascendente).
my_NumList.sort()
print(my_NumList)
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

# Ordenando lista de mayor a menor
# Función: Orden inverso. El argumento 'reverse = True' invierte el criterio de ordenamiento.
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList) # Nota: El print dice de menor a mayor, pero en realidad es de mayor a menor.



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:
# Función general: Mayor eficiencia en memoria y protección de datos fijos contra modificaciones accidentales.

#Convertir una lista a tupla:
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")

# Función: tuple() realiza un casting (conversión). Transforma la lista mutable en una tupla inmutable.
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

# Función: Acceso por índice. La lectura funciona exactamente igual que en las listas.
print(my_tupla[0])
print(my_tupla[2])

# Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
# Función: Operador 'in'. Verifica la existencia de un valor.
print('Rojo' in my_tupla)
# Función: .count() itera la tupla y devuelve la cantidad de veces que aparece un valor específico.
print(my_tupla.count('Rojo'))

# Tupla con un solo elemento
# Al escribir ('Blanco') sin coma, Python lo evalúa como un simple String entre paréntesis.
# Para que sea una tupla de un elemento debe llevar una coma: ('Blanco',)
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria) 

# Empaquetado de tupla, tupla sin paréntesis
# Función: Tuple Packing. Python asume automáticamente que valores separados por comas son una tupla.
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

# Desempaquetado de tupla, se guardan los valores en orden de las variables
# Función: Tuple Unpacking. Asigna los valores de la tupla, uno por uno y en orden, 
# a las variables de la izquierda. (Debe haber la misma cantidad de variables que de valores).
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# Convertir una tupla en una lista
# Función: list() casting inverso. Rompe la inmutabilidad convirtiéndola de nuevo en lista 
# para permitir el uso de métodos como .append() o .remove().
my_lista2=list(my_tupla)
print(my_lista2)
