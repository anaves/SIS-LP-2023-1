"""
Faça um programa para montar a tabela de multiplicação de números de 1 a 10 (ex.: 1 x 1 = 1, 1 x 2 = 2, etc.)
"""

for contador in range(1,11):
    print("="*20)
    print(f"Tabuada do {contador}")
    for fator in range(1,11):
        resultado = contador*fator
        print(f"{contador} x {fator}\t=\t{resultado}")