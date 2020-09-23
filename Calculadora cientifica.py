import math
class calci(object):

    def add(self,num1,num2):
        answer = num1 + num2
        print('Suma = ',answer)
    def sub(self,num1,num2):
        answer = num1 - num2
        print('Diferencia = ',answer)
    def mul(self,num1,num2):
        answer = num1 * num2
        print('Producto = ',answer)
    def div(self,num1,num2):
        answer = num1 / num2
        print('Cociente = ',answer)
    def ln(self,num):
        answer = math.log(num)
        print("ln(%f) = %f" %(num,answer))
    def logten(self,num):
        answer = math.log10(num)
        print("log10(%f) = %f" %(num,answer))
    def logbasex(self,num,x):
        answer = math.log(num,x)
        print("log base(%f)(%f) = %f" %(x,num,answer))
    def squareroot(self,num):
        answer = math.sqrt(num)
        print("Raiz cuadrada(%f) = %f " %(num,answer))
    def powerof(self,num,raiseby):
        answer = math.pow(num,raiseby)
        print("%f ^ (%f) = %f" %(num,raiseby,answer) )
calc = calci()
print('Bienvenido a la calculadora')
print("Listado de operaciones que se pueden realizar")
print('*'*60)
print("1 : Suma  \t\t       6 : Logaritmo base 10")
print("2 : Resta \t           7 : Logaritmo base x")
print("3 : Multiplicacion\t   8 : Raiz cuadrada")
print("4 : Division  \t\t   9 : Potencia de un numero")
print("5 : Logaritmo natural\t")
print('*'*60)
choice = ""
while True:
    try:
        choice = int(input('Selecione un numero de acuerdo a la operacion que desea realizar: '))
    except:
        print("Ingrese un numero valido")
    if choice == 1:
        n1 = float(input('Ingrese el primer numero a sumar : '))
        n2 = float(input('Ingrese el segundo numero a sumar : '))
        calc.add(n1,n2)
    elif choice == 2:
        n1 = float(input('Ingrese el primer numero a restar : '))
        n2 = float(input('Ingrese el segundo numero a restar : '))
        calc.sub(n1,n2)
    elif choice == 3:
        n1 = float(input('Ingrese el primer numero a multiplicar : '))
        n2 = float(input('Ingrese el segundo numero a multiplicar : '))
        calc.mul(n1,n2)
    elif choice == 4:
        n1 = float(input('Ingrese el primer numero a dividir : '))
        n2 = float(input('Ingrese el segundo numero a dividir : '))
        calc.div(n1,n2)
    elif choice == 5:
        n =float(input('Ingrese un numero para encontrar su logaritmo natural : '))
        calc.ln(n)
    elif choice == 6:
        n = float(input('Ingrese un numero para encontrar su logaritmo base 10 : '))
        calc.logten(n)
    elif choice == 7:
        base = float(input('ingrese un valor base : '))
        n = float(input('Ingrese un numero para encontrar su logaritmo en base al valor asignado: '))
        calc.logbasex(n,base)   
    elif choice == 8:
        n = float(input('Ingrese un numero para encontrar su raiz cuadrada : '))
        calc.squareroot(n)    
    elif choice == 9:
        n = float(input('Ingrese un numero  : '))
        po = float(input('Ingrese el numero de potencia a aplicar : '))
        calc.powerof(n,po)
    else:
        print("ADVERTENCIA : Ingrese un numero que se encuentre en la lista")