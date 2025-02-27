palavra = "Thomas"
ganhou = False
chances = 7
letras_usuario = []

while True:
    for letra in palavra:

        if letra.lower() in letras_usuario:
            print(letra, end= " ")
            
        else:
            print("_", end= " ")

    print(f"Você tem: {chances} chances!")
    tentativa = input("Digite uma letra: ")
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1
        print('Errou!')
    else:
        print('Acertou!')

    ganhou = True

    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f'Você ganhou, a palavra é: {palavra}')

else:
    print(f'Você perdeu, a palavra era: {palavra}')
