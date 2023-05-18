"""
Faça um programa para calcular a série de Fibonacci para um número informado pelo usuário, sendo F(0) = 0, F(1) = 1 e F(n)= F(n-1)+F(n-2)
Por exemplo, caso o usuário informe o número 9, o resultado seria:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""
N = int(input("Digite ate a posicao desejada: "))
# Casos iniciais
a = 0
b = 1
# inicio
if N >= 0:
    print(a, end=', ')
if N >= 1:
    print(b, end=', ')
for geracao in range(2,N+1):
    c = a + b
    print(c, end = ", ")
    # atualizar anteriores
    a = b
    b = c
print()
