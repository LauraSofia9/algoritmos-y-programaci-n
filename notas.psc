Algoritmo notas
	Definir notas1, notas2 ,notas3, notas4 Como Real
    Definir i, suma Como Real
    Definir promedio Como Real
    suma <- 0
    Para i <- 0 Hasta 3 Hacer
        Escribir "Ingrese la nota ", i + 1, ":"
        Leer notas
        suma <- suma + notas
    FinPara
    
    promedio <- suma / 4
    Escribir "El promedio es: ", promedio
    
    Si promedio >= 3 Entonces
        Escribir "¡APROBADO!"
    Sino
        Escribir "REPROBADO"
    FinSi
FinAlgoritmo
