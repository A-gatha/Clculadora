print("--------------------------")
print("    PASSOU OU REPROVOU?   ")
print("--------------------------")

mt1 = int(input("Digite sua média do 1° Trimestre: "))
mt2 = int(input("Digite sua média do 2° Trimestre: "))
mt3 = int(input("Digite sua média do 3° Trimestre: "))

ma = ((mt1 * 3) + (mt2 * 3) + (mt3 * 4)) / 10


if ma / 2 >= 6:
    print("Você está Aprovado!")
else:
    print("Você está Reprovado!")