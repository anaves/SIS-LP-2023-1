"""
Faça um programa que leia um número inteiro entre 0 e 9999 e escreva o seu valor por extenso
"""
valor = int(input("digite um valor inteiro entre 0 e 9999: "))
if valor >= 0 and valor <= 9999:
    milhar = valor // 1000
    resto1 = valor%1000
    centenas = resto1//100
    resto2 = resto1%100
    dezenas = resto2//10
    unidades = resto2%10
    if milhar == 9:
        print("nove mil", end=' ')
    elif milhar == 8:
        print("oito mil", end=' ')
    elif milhar == 7:
        print("sete mil", end=' ')
    elif milhar == 6:
        print("seis mil", end=' ')
    elif milhar == 5:
        print("cinco mil", end=' ')
    elif milhar == 4:
        print("quatro mil", end=' ')
    
    if resto1 != 0:
        print("e", end=" ")
        
    ### centenas
    if centenas == 9:
        print("novecentos", end=" ")
    elif centenas == 8:
        print("oitocentos", end=" ")
    elif centenas == 7:
        print("setecentos", end=" ")
    
    ### dezenas
    if dezenas == 9:
        print("noventa", end=" ")
    elif dezenas == 8:
        print("oitenta", end=" ")
    
    ## unidades
    if unidades == 9:
        print("nove")
    elif unidades == 8:
        print("oito")

else:
    print("Voce digitou um valor fora do intervalo")