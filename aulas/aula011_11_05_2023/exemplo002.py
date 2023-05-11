"""
Programa que imprime a soma de todos os números PARES entre dois números quaisquer, incluindo-os
Vamos assumir que num1 < num2
    exemplo num1= 10, num2=40
"""
num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
soma = 0
for i in range(num1, num2+1):
    # verificar se i eh par
    if i%2 == 0:
        print(i)
        soma = soma + i
print(f"A soma dos pares no intervalo [{num1},{num2}] eh {soma}")