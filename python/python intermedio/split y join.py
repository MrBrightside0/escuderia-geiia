##split: de texto a lista
#linea = "estudiar;True"
#partes = linea.split(";")
#print(partes)
#
##con desempaquetado, directo
#texto, hecho = linea.split(";")
#print(texto)
#print(hecho)
#
##join
#print(";".join(["estudiar","True","dormir","False"]))
##estudiar;True;dormir;True
#
##split sin nada parte por espacios
#print("uno dos tres".split())

#Los bugs mas comunes

#una tarea normalida

#ningun que separador es seguro
#linea = "comprar pan; leche;True"
#
#print(linea.split(";"))
#
#texto, hecho = linea.split(";")
#
#guardaron False y lo leyeron de vuelta
#hecho = "False"
#
#print(bool(hecho))
#
#if hecho:
#    print("la marca como hecha")