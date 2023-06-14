""""
Desenvolva um jogo da forca em Python, no qual o programa escolhe aleatoriamente uma palavra secreta de um conjunto pré-definido. O jogador deve tentar adivinhar a palavra digitando letras. Se a letra estiver na palavra secreta, ela deve ser revelada nas posições corretas. Caso contrário, o jogador perde uma vida. O jogo continua até que o jogador adivinhe corretamente a palavra secreta ou perca todas as vidas. O número máximo de vidas deve ser definido pelo programador. O jogo deve exibir uma “representação” da forca conforme o jogador erra letras. Ao final do jogo, o programa deve informar se o jogador venceu ou perdeu, e perguntar se deseja jogar novamente. 
"""
secreta = 'SISTEMAS'
secreta = secreta.upper()
palavra = '*'*len(secreta)
vidas = 10
digitadas = ''
print(palavra)

letra = input('Digite primeira letra: ').upper()
if digitadas.find(letra) >= 0:
    ### que a letra ja foi digitada...
    ### nao aceita
    pass
else:
    digitadas += letra

### verificar se a letra esta na palavra secreta
# aux 
for i in range(len(secreta)):
    if letra == secreta[i]:
        # achou a letra na palavra secreta
        # palavra
        pass
# percorreu todas e nunca achou, dimunui uma vida
vidas -= 1



