"""
Faça um programa para determinar o número de dígitos de um número inteiro positivo informado
ex:
    entrada: 20342 | saida: tem 5 digitos 
    entrada: 2034  | saida: tem 4 digitos
    entrada: -3524 | saida: numero invalido
"""
numero = int(input("digite numero: "))
if numero > 0:
    qtd = 0
    while numero > 0:
        numero = numero // 10
        qtd += 1
    print(f"tem {qtd} digitos")
else:
    print("numero invalido")