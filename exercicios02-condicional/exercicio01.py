# entrada de dados
peso = float(input('Digite peso em kg: '))
altura = float(input('Digite sua altura em m: '))
# processamento
imc = peso / pow(altura,2)

# exemplo de if ternario
#print("PESO NORMAL") if imc <29.9 else print("OBESO")
print(f"IMC calculado {imc}")
if imc < 18.5:
    print("abaixo do peso")
elif imc < 24.9:   #  imc >= 18.5 and imc < 24.9
    print("saudavel")
elif imc < 29.9:
    print("peso em excesso")
elif imc < 34.9:
    print("obesidade GRAU 1")
elif imc < 39.9:
    print("obesidade GRAU 2")
else:
    print("obesidade GRAU 3")