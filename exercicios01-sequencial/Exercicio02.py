#2. Faça um programa que exiba o perímetro de uma circunferência a partir do seu raio 
import math # importar a biblioteca matematica
# entrada de dados
raio = float(input("Informe o raio da circunferencia em metros: "))

# processamento
comprimento  = 2*math.pi*raio

# saida
#print(math.pi)
print(f"o comprimento da circunferencia equivale a {comprimento:.2f}m")