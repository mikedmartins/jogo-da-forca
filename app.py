import random

# Lista de palavras para o jogo da forca
palavras = ['abacaxi', 'banana', 'manga', 'laranja', 'limao']

# Escolha aleatória de uma palavra da lista
palavra = random.choice(palavras)

# Cria uma lista com '_' para cada letra da palavra escolhida
letras_ocultas = ['_'] * len(palavra)

# Número máximo de tentativas
max_tentativas = 6

# Tentativas feitas pelo jogador
tentativas = []

# Loop principal do jogo
while True:
    # Mostra a palavra oculta
    print(' '.join(letras_ocultas))

    # Pede ao jogador para adivinhar uma letra
    letra = input('Digite uma letra: ').lower()

    # Verifica se a letra já foi tentada
    if letra in tentativas:
        print('Você já tentou essa letra, tente outra.')
        continue
    else:
        tentativas.append(letra)

    # Verifica se a letra está na palavra
    if letra in palavra:
        print('Você acertou!')
        # Substitui '_' pela letra acertada
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_ocultas[i] = letra
    else:
        print('Você errou!')
        # Reduz o número de tentativas restantes
        max_tentativas -= 1

    # Verifica se o jogador ganhou ou perdeu
    if '_' not in letras_ocultas:
        print('Parabéns, você ganhou!')
        break
    elif max_tentativas == 0:
        print('Você perdeu! A palavra era:', palavra)
        break
