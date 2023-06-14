"""
Programa para gerar a citação a partir de um nome
– Ex.: Carolina Maria de Jesus à JESUS, C. M. de
Gerar tambem um login: carolina.jesus
"""
nome_completo = " Dorival Moreira Machado Junior   " 
# retirar algum espaco no inicio ou no fim da string
nome_completo = nome_completo.strip()
# separar a string pelo espaco -  dividir a string
partes = nome_completo.split(" ") # split divide texto pelo separador
# print(partes)
# print(partes[0])
# print(partes[-1])
login = partes[0].lower() + "." + partes[-1].lower()
print(login)
citacao = ""
sobrenome = partes[-1]
citacao = sobrenome.upper() + ", "
for indice in range(len(partes)-1):
    parte = partes[indice]
    if parte != 'de' and parte != 'dos':
        citacao =  citacao + parte[0] + ". "
    else:
        citacao =  citacao + parte + " "
print(citacao)