import random

numero_secreto = random.randint(1, 20)

for tentativa in range(5):
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
else:
    print("Você perdeu! O número era:", numero_secreto)