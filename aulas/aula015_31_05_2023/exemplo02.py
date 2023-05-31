# percorrendo uma string
nome = "Dijkstra"
print("forma 1")
for it in range(len(nome)):
    print(f"{it} - {nome[it]}")

print("forma 2")
for letra in nome:
    print(letra)

print("forma 3")
indice = 0
while indice < len(nome):
    print(f"{indice} - {nome[indice]}")
    indice = indice + 1
