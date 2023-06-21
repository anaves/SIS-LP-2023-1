""""
Desenvolva um jogo da forca em Python, no qual o programa escolhe aleatoriamente uma palavra secreta de um conjunto pré-definido. O jogador deve tentar adivinhar a palavra digitando letras. Se a letra estiver na palavra secreta, ela deve ser revelada nas posições corretas. Caso contrário, o jogador perde uma vida. O jogo continua até que o jogador adivinhe corretamente a palavra secreta ou perca todas as vidas. O número máximo de vidas deve ser definido pelo programador. O jogo deve exibir uma “representação” da forca conforme o jogador erra letras. Ao final do jogo, o programa deve informar se o jogador venceu ou perdeu, e perguntar se deseja jogar novamente. 
"""
import os
import requests
import random
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'

response = requests.get(url)

palavras = response.text.split('\n')
secreta = random.choice(palavras).upper()
# print(secreta)
# secreta = 'SISTEMAS'
secreta = secreta.upper()
palavra = '*'*len(secreta)
vidas = 10
digitadas = ''
print(palavra)
erros=['cabeca','tronco', 'perna direita', 'perna esquerda', ' braco direito', 'braco esquerdo', 'olhos', 'nariz', 'boca', 'game over']
while vidas > 0 and palavra != secreta:
    achou = False
    letra = input('Digite primeira letra: ').upper()
    if digitadas.find(letra) >= 0:
        ### que a letra ja foi digitada...
        ### nao aceita
        print('letra ja digitada')
    else:
        digitadas += letra

        ### verificar se a letra esta na palavra secreta
        auxiliar =  list(palavra) 
        for i in range(len(secreta)):
            if letra == secreta[i]:
                # achou a letra na palavra secreta
                # palavra
                auxiliar[i] = letra
                achou = True
        os.system('clear')   # windows.... os.system('cls')
        if not achou:
            vidas-=1
        print(erros[0:10-vidas])

        palavra = ''.join(auxiliar)
        
        print(palavra)

if palavra == secreta:
    print("Parabens voce acertou a palavra secreta")
else:
    print("xiihhhh: perdeu!!!")
    print(secreta)



