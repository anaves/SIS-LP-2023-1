opcao = input('S- somar ou M- multiplicar: ')
if opcao == 'S' or opcao == 'M':
    numero1 = float(input('Primeiro numero: '))
    numero2 = float(input('Segundo numero: '))
    if opcao == 'S':
        resultado = numero1 + numero2
        print(f'Resultado da soma é: {resultado}')
    elif opcao == 'M':
        resultado = numero1 * numero2
        print(f'Resultado da multiplicação é: {resultado}')
else:
    print('Opcao inválida')
print('-----------------------------------------------')