#1- Faça um programa que leia o nome, a idade, a altura, o peso e a nacionalidade do usuário e escreva essas informações na forma de um parágrafo de apresentação
# Entrada de dados
nome = input("Digite o nome: ")
nacionalidade = input("Digite a nacionalidade: ")
idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))

# processamento
#paragrafo = nome + " tem " + str(idade) + " anos"
paragrafo = f"{nome} tem {idade} anos eh {nacionalidade} e sua altura eh de {altura}m e seu peso igual a {peso:.0f} kg"
# saida
print(paragrafo)