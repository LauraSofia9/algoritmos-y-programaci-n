#este va  hacer nuestro programa de estructura de datos
#lista=[]
#tupla=()
#set=
#diccionario={}
import random #sirve para color numeros aleatorios
dado =random.randint (1,6) #esto es para que el dado tire un numero del 1 al 6
print ("el numero del dado es:",dado)

#genere un numero decimal aleatorio entre 0 y 1
decimal=random.random()
print ("el numero decimal es:",decimal)


#escoger un elemento aleatorio de una lista
frutas=["manzana","pera","uva","mango"]
elemento=random.choice(frutas)
print ("la fruta aleatoria es:",elemento)