print("--------------------------")
print("     CALCULADORA CEEP     ")
print("--------------------------")

N1 = int(input("Digite seu Primeiro Número:"))
N2 = int(input("Digite seu Segundo Número:"))

Operador = input('''
Escolha que tipo de operação você deseja:
+ para Adição
- para Subtração
* para Multiplicação
/ para Divisão
''')

if Operador == "+":
    print("{} + {} =".format(N1, N2))
    print(N1 + N2)

elif Operador == "-":
    print("{} - {} =".format(N1, N2))
    print(N1 - N2)

elif Operador == "*":
    print("{} * {} =".format(N1, N2))
    print(N1 * N2)

elif Operador == "/":
    print("{} / {} =".format(N1, N2))
    print(N1 / N2)

else:
    print("Infelizmente esse não é um valor valido, por favor tente novamente usando os caracteres descritos no menu.")