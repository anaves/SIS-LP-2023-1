# entrada de dados
print('-'*50)
altura =  float(input('Digite sua altura em metros: '))
genero = input('Digite o genero (f) ou (m): ')
print('-'*50)

# processamento
peso_h = 72.7*altura-58
peso_m = 62.1*altura-44.7

# saida
if genero.lower() == 'm':
    print(f'Peso ideal (m) de {peso_h:.1f} kg')
#if genero == 'f':
else: # caso contrario
    print(f'Peso ideal (f) de {peso_m:.2f} kg')

print('-'*50)