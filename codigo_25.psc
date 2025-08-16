Algoritmo codigo_25
	Definir i, numero Como Entero
    
    Escribir "Ingrese 10 números:"
    
    Para i <- 1 Hasta 10 Hacer
        Escribir "Ingrese el número ", i, ":"
        Leer numero
        
        Si numero MOD 2 = 0 Entonces
            Escribir "Número par encontrado: ", numero
        FinSi
    FinPara
FinAlgoritmo
