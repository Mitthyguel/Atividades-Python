frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print("Número de vogais:", contador)