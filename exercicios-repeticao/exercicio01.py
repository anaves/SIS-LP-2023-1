"""
Faça um programa que gere números inteiros aleatórios entre 1 e 10 e calcule a soma desses números, até que seja gerado um número num que foi informado pelo usuário anteriormente.
----Dica 1: antes de mais nada, peça para o usuário digitar um número entre 1 e 10 e guarde o valor em num
----Dica2: use a função randint(inicio, fim) do módulo random para gerar um número aleatório entre 1 e 10
"""
# importacoes de bibliotecas
import random  # biblioteca util pra trabalhar com valores aleatorios
# inicializar a variavel soma
soma = 0 

print("="*30)
num_sorte = int(input("digite o numero da sorte: "))
while num_sorte < 1 or num_sorte >10:
    # quando num_sorte for invalido
    print("numero invalido, digite um valor entre 1 e 10")
    num_sorte = int(input("digite o numero da sorte: "))
print("="*30)

sorteado = random.randint(1,10)
while sorteado != num_sorte:
    soma = soma + sorteado
    print(f"soma parcial = {soma} sorteado {sorteado}")
    sorteado = random.randint(1,10)

print(f"A soma final foi de {soma}")