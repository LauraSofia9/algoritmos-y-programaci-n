Algoritmo contador_de_negativos
	Definir numero Como Entero
    Definir contadorNegativos Como Entero
    
    contadorNegativos <- 0
    
    Escribir "Ingrese n�meros (ingrese 0 para terminar):"
    
    Repetir
        Escribir "Ingrese un n�mero:"
        Leer numero
        
        Si numero < 0 Entonces
            contadorNegativos <- contadorNegativos + 1
        FinSi
    Hasta Que numero = 0
    
    Escribir "La cantidad de n�meros negativos ingresados es: ", contadorNegativos
FinAlgoritmo
