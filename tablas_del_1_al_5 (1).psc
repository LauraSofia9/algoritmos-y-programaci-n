Algoritmo tablas_del_1_al_5
	Definir  numero, i Como Entero
	Escribir "Ingrese un número para mostrar su tabla de multiplicar (del 1 al 5):"
	leer numero
	Escribir "tabla de multiplicar del " ,numero, ":"
	para i<- 1 hasta 10 con paso 1 hacer 
		escribir numero, " x ", i, " = ", numero * i
	FinPara
	
FinAlgoritmo
