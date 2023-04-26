# entrada de dados
print('-'*50)
altura =  float(input('Digite sua altura em metros: '))
print('-'*50)

# processamento
peso_h = 72.7*altura-58
peso_m = 62.1*altura-44.7

# saida
print(f'Peso ideal (h) de {peso_h:.1f} kg')
#print('Peso ideal (m) de ', peso_m, ' kg')
print(f'Peso ideal (m) de {peso_m:.2f} kg')
print('-'*50)