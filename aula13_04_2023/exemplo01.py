"""
Identifique se numero informado e' par
"""
# entrada
numero = int(input('Digite valor: '))
# processamento
resto = numero%2
condicao = resto == 0
if condicao:
    # INDENTACAO
    print(f"{numero} par")

print('fim da execucao')

