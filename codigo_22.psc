Algoritmo suma_de_5_n�meros
	definir numero, suma, contador Como Entero
	escribir  "digite 5 n�meros que desee sumar: "
	contador <- 1
	Mientras contador <= 5  Hacer
		escribir " numero " , contador, ":"
		leer numero
		suma <- suma + numero
		contador <- contador + 1
		
	Fin Mientras
	escribir " la suma total es: " ,suma
FinAlgoritmo
