# Agora vamos calcular a média de três notas fornecidas na entrada do usuário.

print("------#--------#--------#--------#------")
print("Agora vamos calcular a média de três notas fornecidas na entrada do usuário.")
print("------#--------#--------#--------#------")

nota1 = None
nota2 = None
nota3 = None

while nota1 is None:
    try:
        nota1 = float(input("Digite a primeira nota: "))
    except ValueError:
        print("Valor inválido. Digite um número válido.")

while nota2 is None:
    try:
        nota2 = float(input("Digite a segunda nota: "))
    except ValueError:
        print("Valor inválido. Digite um número válido.")

while nota3 is None:
    try:
        nota3 = float(input("Digite a terceira nota: "))
    except ValueError:
        print("Valor inválido. Digite um número válido.")

media = (nota1 + nota2 + nota3) / 3

print("A média das notas é:", media)