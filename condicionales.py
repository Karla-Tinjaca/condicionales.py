# escribir el algoritmo para saber si el algoritmo para saber si el numero ingresado por el teclado es positivo o negativo
numero = float (input("digite un numero: "))
if numero > 0: 
    print ("el numero es positivo")
elif numero == 0:
   print ("el numero es igual a cero")
else: 
 print ("el numero es negativo")

 # escribir un algoritmo que reciba dos numeros por teclado y diga cual es mayor y cual es menor 
numero_1 = float (input ("digite un numero: "))
numero_2 = float (input ("digite un numero: "))
if numero_1 > numero_2:
   print ("El numero es mayor")
elif numero_1 < numero_2:
   print ("El numero es menor")
else:
   print("Los numeros son iguales")

# escriba un programa que lea tres numeros enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos
a = int(input ("digite un numero: "))
b = int(input ("digite un numero: "))
c = int(input ("digite un numero: "))
menor = a
mayor = a
if b < menor:
   menor = b
elif b > mayor:
   mayor = b
if c < menor: 
   mayor = c 
elif c > mayor: 
   mayor = c
print (" el menor numero es" , menor)
print ("el mayor numero es" , mayor)

# dados dos numeros A y B, sumarlos si A es menor que B o sino restarlos
a = float(input ("digite un numero: "))
b = float(input("digite un numero: "))


if a > b:
   resultado = a + b
elif a < b:
   resultado = a - b 
else:
   resultado = 0 
   print ("Los numeros son iguales")
print("el resultado es:", resultado)

#Dados dos numeros A y B Encontrar el cociente entre A y B. Recordar que la division por 0 no esta definida, 
#en ese caso debe aparecer una leyenda anunciando que la division no es posible.

a = float (input ("digite un numero: "))
b = float (input ("digite un numero: "))

if a == 0: 
   print ("No se puede divir por cero")
elif b == 0:
   print ("No se puede divir por cero")
else:
   resultadoDivision = a / b 
   print ("el resultado es: " , resultadoDivision)

#Dados dos numeros A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario, multiplicarlos.
   
a = float (input ("digite un numero: "))
b = float (input ("digite un numero: "))

if a < 0:
   resultdoSuma = a + b 
   print ("la suma de los numeros es: " , resultdoSuma)
elif b < 0:
   resultdoSuma = a + b 
   print ("la suma de los numeros es: " , resultdoSuma)
else: 
   resultadoMultiplicacion = a * b 
   print ("la multiplicacion de los numeros es: " , resultadoMultiplicacion)


#Escribir un algoritmo que determine si un año es bisiesto o no
año = int (input ("Digite el año: "))
 
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
	print("Es bisiesto")
else:
	print("No es bisiesto")

   



