

#    1. Una lista guarda varias cosas en una sola variable. 

#    2. Cada elemento tiene una posición, y se empieza a contar en 0.

#    3. La lista se puede modificar después de creada:
#                                         agregar, quitar, cambiar. Es su diferencia principal con el texto



#--------------------------------------------------------------------------------------------------------------------------------


#Una lista guarda varias cosas en una sola variable. 
# Se escribe con corchetes y comas. Puede mezclar tipos, aunque casi siempre no conviene

cast_hamilton= ['Hamilton', 'Burr', 'Eliza', 'Angelica', 'George', 'Lafayette', 'Jefferson']

#--------------------------------------------------------------------------------------------------------------------------------

#Puede mezclar tipos, aunque casi siempre no conviene

cast_hamilton= [ 51, 'Burr', True, 'Angelica', 0.342, 'Lafayette', 'Jefferson']
#               int         bool               float      str

'''
print(cast_hamilton[0])
print(cast_hamilton[1])
print(cast_hamilton[2])
print(cast_hamilton[4])
'''
#--------------------------------------------------------------------------------------------------------------------------------


#Cada elemento tiene una posición, y se empieza a contar en 0.

cast_hamilton= ['Hamilton', 'Burr', 'Eliza', 'Angelica', 'George', 'Lafayette', 'Jefferson']
#                   0           1       2       3           4           5           6 | -1

'''
print(cast_hamilton[0]) #Hamilton 


print("")
print(cast_hamilton[-1]) #Jefferson
print(cast_hamilton[6]) #Jefferson

# Algo importante de utilzar negativos, o lo bueno, es que te van a dar el valor en reversa 
# O mas en especifico "len - N", N siendo el numero de lugar que quieres saber una cantidad de lugares antes del final

print(cast_hamilton[-2])
print(cast_hamilton[-3])

#IndexError
print(cast_hamilton[10])


#IndexError
print(cast_hamilton[-8])
print(cast_hamilton[-10])
'''
#--------------------------------------------------------------------------------------------------------------------------------


#print(len(cast_hamilton))


# El ultimo numero que existe en una lista es "len - 1"
# O en otras palabras, lo que len te va a arrojar es el ultimo numero de una lista + 1



#--------------------------------------------------------------------------------------------------------------------------------


#La lista se puede modificar después de creada:
#                                         agregar, quitar, cambiar. Es su diferencia principal con el texto



#-----------------------------------
cast_hamilton.append("Madison") #Esto es para anadir una cosa nueva a la lista, va al final de la lista 

#cast_hamilton= ['Hamilton', 'Burr', 'Eliza', 'Angelica', 'George', 'Lafayette', 'Jefferson', 'Madison']
#                     0         1       2          3          4          5            6         7| -1

'''
print(cast_hamilton[7]) 
print(cast_hamilton[-1])
print(cast_hamilton[0])
'''
#-----------------------------------

cast_hamilton.remove("George") #Esto es para ELIMINAR la cosa escrita de la lista, todo se recore a la izquierda 

#ANTES:

#cast_hamilton= ['Hamilton', 'Burr', 'Eliza', 'Angelica', 'George', 'Lafayette', 'Jefferson', 'Madison']
#                     0         1       2          3          4          5            6          7| -1


#DESPUES:

#cast_hamilton= ['Hamilton', 'Burr', 'Eliza', 'Angelica', 'Lafayette', 'Jefferson', 'Madison']
#                     0         1       2          3           4            5         6| -1

'''
print(cast_hamilton[4]) 
print(cast_hamilton[-1])
print(cast_hamilton[0])
'''
#INDEX ERROR
#print(cast_hamilton[7])

#-----------------------------------

cast_hamilton[5]= 'King George III'

#print(cast_hamilton[5])


#-----------------------------------

#cast_hamilton= ['Hamilton', 'Burr', 'Eliza', 'Angelica', 'Lafayette', 'King George III', 'Madison']
#                     0         1       2          3           4            5         6| -1

cast_hamilton.insert(4, "George") #(posicion, coso)

# la lista se recorre a la izquiera 

#Antes 
#cast_hamilton= ['Hamilton', 'Burr', 'Eliza', 'Angelica', 'Lafayette', 'King George III', 'Madison']
#                     0         1       2          3           4            5               6| -1

#Despues
#cast_hamilton= ['Hamilton', 'Burr', 'Eliza', 'Angelica', 'George' 'Lafayette', 'King George III', 'Madison']
#                     0         1       2          3          4          5             6              7| -1

'''
print(cast_hamilton[4]) 
print(cast_hamilton[-1])
print(cast_hamilton[7])
print(cast_hamilton[0])
'''

#-----------------------------------

#print(cast_hamilton.index('Madison'))


cast_hamilton= ['Hamilton', 'Burr', 'Eliza', 'Angelica','Lafayette', 'King George III', 'Madison', 'George']

#print(cast_hamilton.index('George'))




#Ejercicio


#hagan una lista de sus cosas en la mochila

mochila=['agua', 'libretas', 'calculadora', 'lapiz', 'sacapuntas', 'cuaderno', 'lapicera']

#print( mochila[0])
#print( mochila[-1])
#print(len(mochila))

mochila.append('borrador')
mochila.remove('agua')


#mochila=['libretas', 'calculadora', 'lapiz', 'sacapuntas', 'cuaderno', 'lapicera', 'borrador']
#print(mochila)

numero_de_cosas= len(mochila)

#print(mochila[int((numero_de_cosas/2))])
