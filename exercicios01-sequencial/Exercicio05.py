"""5- Faça um programa para, a partir de um valor informado em centavos, indicar a menor quantidade de moedas que representa esse valor
- Considere moedas de 1, 5, 10, 25 e 50 centavos, e 1 real
- Exemplo: para o valor 290 centavos, a menor quantidade de moedas é 2 moedas de 1 real, 1 moeda de 50 centavos, 1 moeda de 25 centavos, 1 moeda de 10 centavos e 1 moeda de 5 centavos
"""
# entrada de dados
print("-----DPM - Dispensador Preciso de Moedas-----")
valor = int(input('Informe um valor em centavos: R$ '))
print('----------------------------------------------')
moedas_1real = valor//100 # // me devolve somente a parte inteira da divisao, ex: 292/100 = 2.92   292//100 = 2
resto = valor%100  # % eh o operador que calcula o resto da divisao
moedas_50cents = resto//50
resto = resto%50
moedas_25cents = resto//25
resto = resto%25
moedas_10cents = resto//10
resto = resto%10
moedas_5cents = resto//5
moedas_1cent = resto%5
# saida de dados
print(f'{moedas_1real} moedas de R$ 1,00')
print(f'{moedas_50cents} moedas de R$ 0,50')
print(f'{moedas_25cents} moedas de R$ 0,25')
print(f'{moedas_10cents} moedas de R$ 0,10')
print(f'{moedas_5cents} moedas de R$ 0,05')
print(f'{moedas_1cent} moedas de R$ 0,01')
