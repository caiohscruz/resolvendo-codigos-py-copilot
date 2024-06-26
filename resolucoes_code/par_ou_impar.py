# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 

print("------#--------#--------#--------#------")
print("Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.")
print("------#--------#--------#--------#------")

num = input("Digite um número inteiro: ")

try:
    num = int(num)
    if num % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")