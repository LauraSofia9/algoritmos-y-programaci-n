Algoritmo cajero
	Definir claveIngresada Como Entero
    Definir claveCorrecta Como Entero
    claveCorrecta <- 1234
    
    Escribir "BIENVENIDO. Ingrese su clave (3 intentos):"
    
    Para intento <- 1 Hasta 3 Hacer
        Leer claveIngresada
        Si claveIngresada = claveCorrecta Entonces
            Escribir "Acceso permitido. Bienvenido."
            intento <- 4 
        Sino
            Escribir "Clave incorrecta. Intentos restantes: ", 3 - intento
        FinSi
    FinPara
FinAlgoritmo
