#este es mi programa que refuerza listas
estudiante={
    "hernan Dario":"Toolkit",
    "edad": 18, 
    "carrera": "Ingenieria de sistemas",



}
print("Nombre", estudiante["hernan Dario"])
#agreagar un elemento al diccionario
estudiante["nota"]=90
#recorrer cada posicion del diccionario
for clave, valor in estudiante.items():
    print(clave, ":", valor)