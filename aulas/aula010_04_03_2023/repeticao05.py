"""
Fatorial de um número
ex:  
definido que 0!= 1
definido que 1! = 1*0! = 1*1 = 1
exemplos:
2! = 2*1! = 2*1 = 2
3! = 3*2! = 3*2*1 = 6
4! = 4*3*2*1 = 24
5! = 5*4*3*2*1 = 120
"""
msg = "***** Calcula Fatorial do numero *****"
print("-"*len(msg))
print(msg)
num = int(input("Digite numero:"))
# processo
fatorial = 1
iterador = 1
while iterador <= num:
    fatorial = fatorial * iterador
    iterador += 1  # iterador = iterador + 1
print(f'{num}! = {fatorial}')
print("-"*len(msg))