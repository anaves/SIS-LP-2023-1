"""
E se o enunciado fosse “Faça um programa que soma X números gerados aleatoriamente no intervalo de 1 a 10, onde X é informado pelo usuário”?
"""
######## REPETICAO CONTAVEL --- posso utilizar o a estrutura for
import random
x = int(input("Digite a qtd de numeros: "))
soma = 0

### REPETICAO CONTAVEL!!!
for contador in range(x):
    sorteado = random.randint(1,10)
    print(contador)
    #print(f"sorteado {sorteado}")
    soma = soma + sorteado
print(f"a soma foi de {soma}")
