Algoritmo codigo_25
	Definir i, numero Como Entero
    
    Escribir "Ingrese 10 n�meros:"
    
    Para i <- 1 Hasta 10 Hacer
        Escribir "Ingrese el n�mero ", i, ":"
        Leer numero
        
        Si numero MOD 2 = 0 Entonces
            Escribir "N�mero par encontrado: ", numero
        FinSi
    FinPara
FinAlgoritmo
