Algoritmo muralla
	definir num como entero 
	pares <- 0
	impares <- 0 
	para i <- 1 hasta 10 con paso 1 
		leer num 
		si num MOD 2 = 0 entonces
			pares <- pares + 1
		sino  impares <- impares + 1 
		FinSi
	FinPara
	escribir "pares: "  , pares,  " impares: " , impares
FinAlgoritmo
