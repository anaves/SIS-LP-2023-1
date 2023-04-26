"""
Identifique se numero informado e' par ou impar
"""
# entrada
numero = int(input('Digite valor: '))
# processamento
resto = numero%2
#condicao = resto == 0
if resto == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é impar")

print('fim da execucao')

