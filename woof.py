#ejercicio 1

def factorial(n):
    if n==0 or n==1:
        return 1
    a = n
    b = n
    while a>1:
        a = a-1
        b = a*b
    return b

def factorial2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial2(n-1)
print factorial(5)


# ejercicio 2

def rfc ():
    nombre = raw_input ("Escribe tu nombre: ")
    apellido1 = raw_input ("Escribe tu primer apellido: ")
    apellido2 = raw_input ("Escribe tu segundo apellido: ")
    dia = raw_input ("Escribe tu dia de nacimiento: ")
    mes = raw_input ("Escribe tu mes de nacimiento: ")
    anho = raw_input ("Escribe tu año de nacimiento: ") 
    n = nombre [:1]
    a1 = apellido1 [:2]
    a2 = apellido2 [:1]
    d = dia
    m = mes
    a = anho [2:]
    resultado = a1+a2+n+a+m+d
    print resultado


rfc ()
    
