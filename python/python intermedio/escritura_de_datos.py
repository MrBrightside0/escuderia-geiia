#tareas = ["estudiar", "dormir", "lavar los trastes", "hola"]
#
##"w" Escribir desde 0 BORRA TODO EL CONTENIDO ANTERIOR Y SOBRESCRIBE
#with open("tareas.txt", "w") as f:
#    for t in tareas:
#        f.write(t + "\n")
        

# "a" agregar al final, lo que ya se conserva mas la linea que agregues
#with open("tareas.txt", "a") as f:
#    f.write("hola x2")

#"x" crear y falla si existe, util para cuando no sabes que haces 
#with open("importante.txt", "x") as f:
#    f.write("Hola")
    
#Leer
#with open("importante.txt") as f:
#    contenido = f.read()
#    
#print(contenido) 

#with open("importante1.txt", "w") as f:
#    f.write("datos valiosos \n")
    
#pass literalmente no hace nada    
#with open("importante1.txt", "w") as f:
#    pass    
    
#otra forma de leer archivos    
#print(open("importante1.txt").read())


#un archivo se recorre como una lista
tareas = []
#
#with open("tareas.txt") as f:
#    for linea in f:
#        tareas.append(linea.strip())
#        
#print(tareas) # ['estudiar', 'dormir', 'lavar los trastes']

#si el archivo

#introduccion excepcion
try:
    with open("archivo_que_no_existe.txt") as f:
        for linea in f:
            tareas.append(linea.strip())
except FileNotFoundError:
    print("Eres un menso, escribe bien la ruta")
    
#utilicen .strip .lower      
#almacenar los datos en archivo