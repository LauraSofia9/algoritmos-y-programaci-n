#mi tercer_codigo
print("hola, bienvenido")
while True:
    edad=int(input("imgresa tú edad:"))
    if edad > 0 and edad <120:
        edad_futura =edad + 5
        print("En 5 años tendras" , edad_futura )
        break
    else:
        print("por favor ingrese una edad valida (entre 1 y 120)")



