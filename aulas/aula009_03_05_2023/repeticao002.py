"""
Programa que imprime a quantidade de números pares de 100 até 200, incluindo-os
"""
iterador = 100
contador_pares = 0
while iterador <= 200:
    # e' par, quando o resto da divisao por 2 e' 0
    if iterador%2 == 0:
        contador_pares += 1
        print(f'{iterador} par')
    else:
        print(f'{iterador} impar')

    iterador = iterador + 1
#### FIM DO WHILE
print(f'Temos {contador_pares} numeros pares neste intervalo')