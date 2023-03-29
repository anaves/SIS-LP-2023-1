"""
Exemplo de comentario de bloco, utilize " 3x no inicio e 3x ao final do comentario
4- Faça um programa que informe a distância em quilômetros de um raio para o observador 
- O observador deve informar o tempo (em segundos) transcorrido entre ver o raio e ouvir o trovão
- Assuma que a velocidade do som é 340 m/s
"""
# entrada de dados
print('='*60)
tempo = int(input('Tempo (em segundos) ate ouvir o trovao: '))

# processamento
distancia = 340/tempo
distancia_km = distancia/1000

# saida de dados
print(f'Distancia em metros: {distancia} m')
print(f'Distancia em quilometros: {distancia_km} km')