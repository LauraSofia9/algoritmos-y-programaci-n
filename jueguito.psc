Algoritmo jueguito
	definir puntos, enemigosDerrotados Como Entero
	definir premioActivado Como Logico
	puntos <- 0
	enemigosDerrotados <- 0
	premioActivado <- Falso
	escribir "¡Bienvenido compañero! Derrota enmigos para ganar puntos"
	Repetir
		escribir"____________________________"
		escribir"puntos actuales: ", puntos
		escribir "Enemigos derrotados: ", enemigosDerrotados
		escribir" Presiona [1] para atacar o [0] para salir"
		leer opción
		si opción == 1 entonces enemigosDerrotados<- enemigosDerrotados + 1
			puntos <- puntos + 2 //suponemos que cada enemigo da dos puntos
			si puntos MOD  5 == 0 y puntos > 0 Entonces
				si  premioActivado  == Falso Entonces//EVITAR REPETIR EL MENSAJE
					escribir" ¡premio! has ganado + 1 vida (puntos: " , puntos, ")"
					premioActivado <- verdadero
				FinSi
			sino  premioActivado <- falso//Reinicia  para el proximo premio.
			FinSi
		FinSi
	Hasta Que  opción == 0 
	escribir " Juego terminado. puntos totales: ", puntos 
	
FinAlgoritmo
