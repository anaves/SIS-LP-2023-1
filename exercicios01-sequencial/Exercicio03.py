#3. Faça um programa que leia dois pontos num espaço bidimensional e calcule a distância entre esses pontos
# importando a biblioteca matematica
import math
# entrada de dados
print("-"*50)
latitude1 = float(input('Latitude do ponto 1: '))
longitude1 = float(input('Longitude do ponto 1: '))
print("-"*50)
latitude2 = float(input('Latitude do ponto 2: '))
longitude2 = float(input('Longitude do ponto 2: '))
print("-"*50)
# processamento
# sqrt  - square root -- > raiz quadrada
distancia = math.sqrt((latitude1-latitude2)**2+(longitude1-longitude2)**2)
# saida de dados
print(f'A distancia entre o ponto 1 ({latitude1},{longitude1}) e o ponto 2 ({latitude2},{longitude2}) eh {distancia}')