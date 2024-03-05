print("------------------------")
print("  QUAL NÚMERO É MAIOR?  ")
print("------------------------")

N1 = float(input("Digite o primeiro número para a verificação: "))
N2 = float(input("Digite o segundo número para a verificação: "))

if N1 > N2:
    print("O número ", N1, " é o maior número")
    print("--------------------")
    print(" FIM DA VERIFICAÇÃO ")
    print("--------------------")
elif N1 == N2:
    print('Ambos os números são iguais')
    print("--------------------")
    print(" FIM DA VERIFICAÇÃO ")
    print("--------------------")
else:
    print("O número ", N2, " é o maior número")
    print("--------------------")
    print(" FIM DA VERIFICAÇÃO ")
    print("--------------------")

    
