"""
Programa que imprime a soma de todos os números pares entre dois números quaisquer, incluindo-os
"""
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

iterador = min(valor1,valor2)

soma = 0
while iterador <= max(valor1,valor2):
    # e' par, quando o resto da divisao por 2 e' 0
    if iterador%2 == 0:
        #contador_pares += 1
        soma = soma + iterador  #  faz a soma acumulada
    iterador = iterador + 1

#### FIM DO WHILE
## imprimir a soma dos pares no intervalo
print(f'A soma dos numeros pares igual a {soma}')