nome = "Maria Silva"
# operador len -> devolve o comprimento da string
tamanho = len(nome)
for indice in range(tamanho):
    letra = nome[indice]
    print(f"{indice}= {letra}")

chave = 'Sil'
# operador in -> retorna True se a substring for parte de string e False caso contrario
if chave in nome:   
    print(f"{chave} ESTA presente em {nome}")
else:
    print(f"{chave} NAO ESTA presente em {nome}")

if chave not in nome:
    print(f"{chave} NAO ESTA presente em {nome}")
else:
    print(f"{chave} ESTA presente em {nome}")

# +   operador de concatenacao -> juntar
primeiro_nome = "Alan"
sobrenome = "Turing"
nome_completo = primeiro_nome + sobrenome
print(nome_completo)
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo)

# * operador que repete a string int vezes
padrao = "lobo"
padrao_repetido = padrao*2
print(padrao_repetido)
padrao_repetido = padrao*5
print(padrao_repetido)