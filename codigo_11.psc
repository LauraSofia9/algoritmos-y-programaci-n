Algoritmo par_impar
	definir num, resultado Como Entero
	escribir "ingrese el número"
	leer num
	
	resultado <- num mod 2 
	si resultado = 0 entonces 
		escribir "el número es par"
	sino 
		escribir " el número es impar"
	FinSi
	
FinAlgoritmo
