# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

print("------#--------#--------#--------#------")
print("Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles")
print("------#--------#--------#--------#------")

#Prompt: Crie uma aplicação simples que receba dois números e permita o usuário selecionar a operação que será realizada com eles. Apresente o resultado em tela.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite o número da operação desejada: "))

if opcao == 1:
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)
elif opcao == 2:
    resultado = num1 - num2
    print("O resultado da subtração é:", resultado)
elif opcao == 3:
    resultado = num1 * num2
    print("O resultado da multiplicação é:", resultado)
elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)
    else:
        print("Não é possível dividir por zero.")
else:
    print("Opção inválida. Por favor, selecione uma opção válida.")