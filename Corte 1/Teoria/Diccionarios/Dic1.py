# Función: Inicialización estándar de diccionarios. 
# Mapea strings (identificadores) a enteros (datos). Ideal para guardar el último 
# estado leído de los sensores del ESP32 sin tener que usar múltiples variables sueltas.
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)

# Función: Mapeo String-String. Diccionario básico de equivalencias.
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
print(translations)

## Verifiying an error:
# Función: Demuestra la regla de inmutabilidad (Hashable).
# Esta línea se mantiene comentada para que el código funcione. 
# Las claves NO pueden ser listas. Daría TypeError.
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# print(powers)

# Función: Estructuras Anidadas (Listas como Valores). 
# Las claves son estrictas, pero los valores son libres. Acá agrupo múltiples datos 
# bajo un mismo identificador.
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

# Función: Inicializar diccionario vacío. 
# Lo uso cuando voy a recolectar datos dinámicamente dentro de un bucle 'for' o 'while'.
my_empty_dictionary = {}
print(my_empty_dictionary)

# Función: Inserción directa. Crea una nueva clave O(1) asignándole un valor.
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["cheesecake"] = 8
print("After", menu)

# reasigna toda la variable.
# La variable 'animals_in_zoo' se destruye y se vuelve a crear con un nuevo diccionario cada vez.
# El resultado final será solo {"horses": 2}.
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)

## Add multiple keys
# Función: .update() para inserción masiva. 
# Fusiona un diccionario nuevo dentro del existente. Mucho más eficiente.
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

# If we wanted to add 3 new rooms, we could use:
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors)

###
# Función: Verificación del comportamiento de .update() ampliando registros.
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

## Overwrite Values ##
# Función: Mutación (Sobrescritura). 
# Si la clave "oatmeal" ya existe, reasigna su puntero en memoria al nuevo valor (5). No duplica.
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["oatmeal"] = 5
print("After", menu)

## Notice the value of "oatmeal" has now changed to 5.
# Función: Comparativa de actualización. 
# Demuestra que .update() (agrega) y el acceso directo [] (sobrescribe) pueden usarse en conjunto.
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)

### Dict Comprehensions
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# Función: zip() crea un iterador que empareja elementos de ambas listas índice por índice.
zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)

# Función: Dict Comprehension. Sintaxis avanzada para iterar sobre el objeto zip y armar 
# el diccionario al vuelo en una sola línea.
students = {key:value for key, value in zip(names, heights)}
print(students)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Función: Mismo proceso de zip + comprensión, pero desglosado en variables.
zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks) # Imprime el objeto de memoria (<zip object>), no su contenido visual.

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

# Función: Flujo completo de trabajo (zip, inserción, sobrescritura y anidación).
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# 1. Empareja con zip y comprensión.
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)

# 2. Modifica el diccionario recién creado.
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After: ", plays)

# 3. Anidación profunda. Asigna diccionarios como valores.
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
