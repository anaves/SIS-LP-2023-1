"""
Faça um programa para calcular a série de Fibonacci para um número informado pelo usuário, sendo F(0) = 0, F(1) = 1 e F(n)= F(n-1)+F(n-2)
Por exemplo, caso o usuário informe o número 9, o resultado seria:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

a = 0
b = 1
# inicio
print(a, end=', ')
print(b, end=', ')
" geracao 2"
c = a + b
print(c, end = ", ")
# atualizar
a = b
b = c
# geracao 3
c = a+b
print(c, end = ", ")
# atualizar
a = b
b = c
# geracao 4
c = a+b
print(c, end = ", ")
# atualizar
a = b
b = c
print()