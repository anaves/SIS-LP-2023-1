import requests
import random
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'

response = requests.get(url)
#print(response.text)
palavras = response.text.split('\n')
#n_palavras = len(palavras) # pega a qtd de palavras
#posicao_sorteada =  random.randint(0, n_palavras) # sorteia uma posicao
#print(palavras[posicao_sorteada])\

secreta = random.choice(palavras).upper()
print(secreta)