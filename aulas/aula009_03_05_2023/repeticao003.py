"""
DESAFIO!!!
Como fazer para contar a quantidade de números pares entre dois números quaisquer?
"""
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

iterador = min(valor1,valor2)

contador_pares = 0
while iterador <= max(valor1,valor2):
    # e' par, quando o resto da divisao por 2 e' 0
    if iterador%2 == 0:
        contador_pares += 1
        print(f'{iterador} par')
    else:
        print(f'{iterador} impar')

    iterador = iterador + 1
#### FIM DO WHILE
print(f'Temos {contador_pares} numeros pares neste intervalo')