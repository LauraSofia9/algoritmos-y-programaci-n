Algoritmo contador_de_negativos
	Definir numero Como Entero
    Definir contadorNegativos Como Entero
    
    contadorNegativos <- 0
    
    Escribir "Ingrese números (ingrese 0 para terminar):"
    
    Repetir
        Escribir "Ingrese un número:"
        Leer numero
        
        Si numero < 0 Entonces
            contadorNegativos <- contadorNegativos + 1
        FinSi
    Hasta Que numero = 0
    
    Escribir "La cantidad de números negativos ingresados es: ", contadorNegativos
FinAlgoritmo
