# titulo del programa 

print("*"*60)
print("Calculadora 01")
print("*"*60)

# solicitar datos por consola
numero1 = float(input("introducir el primer numero:"))
numero2 = float(input("introducir el segundo numero:"))

#imprimir opperatoria
print("la suma es:", numero1+numero2)
print("la resta es:", numero1-numero2)
print("la multiplicacion es:", numero1*numero2)
print("la division es:", numero1/numero2)

# este input mantiene abierto el programa
input()

if __name__ == '__main__':
	main()