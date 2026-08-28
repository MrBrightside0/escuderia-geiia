#Usando for, hay que sumar todos los numeros del 1 al 100 (se puede imprimir cada uno o la suma final de todos)

#i = 1,2,3,4,5,6,

#✅
x = 0
for i in range(1,101):
    x = x + i
    print(x)
    

#
for i in range(1,101):
    x = i - 1 + i
    print(x)
    
    
#    
x = 0
for i in range(1,101):
    x = x + (i + (i + 1))
    
print(x / 2)