altura = input('Digite a altura do triangulo: ')  # entrada
base = float(input('Digite a base do triangulo: ')) # entrada
print(type(altura))
altura = float(altura) # mudanca de tipo (conversao de tipo)
print(type(altura))
print(altura)   # saida
print(base)
area = (base*altura)/2 # processamento
print("\nCalculo da area do\ttriangulo")     # saida
print("="*40)
print(f"A area do triangulo eh {area}")

