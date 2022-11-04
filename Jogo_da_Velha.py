# Feito por Leoxy (https://github.com/LeoxyOF)

lista_de_numeros = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
o = x = 0


def primeiro_a_jogar():
    from random import choices
    from time import sleep
    print("Tabela: ")
    print("""
1  |  2  |  3
---|-----|---
4  |  5  |  6
---|-----|---
7  |  8  |  9""")
    print()
    sleep(1)
    print("=" * 30)
    print("Primeiro Jogador".center(30))
    print("=" * 30)
    print("Escolhendo primeiro a jogar....")
    sleep(2)
    escolhido = choices(["X", "O"])
    print(f'\nO escolhido foi o jogador "{escolhido[0]}"')
    return escolhido[0]


def interface_e_posicoes(pos, simbolo):
    for posicoes in range(1, 10):
        if pos == posicoes:
            lista_de_numeros[pos - 1] = simbolo
    print(f"""
{lista_de_numeros[0]}  |  {lista_de_numeros[1]}  |  {lista_de_numeros[2]}
---|-----|---
{lista_de_numeros[3]}  |  {lista_de_numeros[4]}  |  {lista_de_numeros[5]}
---|-----|---
{lista_de_numeros[6]}  |  {lista_de_numeros[7]}  |  {lista_de_numeros[8]}""")


def checar_resposta(entrada, simbolo):
    while True:
        try:
            resp = int(input(entrada))
            if lista_de_numeros[resp - 1].isalpha():
                print("Essa posição está ocupada!")
                continue
            else:
                interface_e_posicoes(resp, simbolo)
                break
        except (ValueError, TypeError):
            print("Digite um valor válido!")
        except IndexError:
            print("Digite Apenas um Valor!!")
            continue


def checar_vitoria(lista):
    vertical1 = vertical2 = vertical3 = ''
    horizontal1 = horizontal2 = horizontal3 = ''
    diagonal1 = diagonal2 = ''
    vitoria = False
    simbolo = ''
    conferir_empate = ''
    for posicao, valor in enumerate(lista):
        # horizontal
        if posicao in [0, 1, 2]:
            horizontal1 += str(valor)
        if posicao in [3, 4, 5]:
            horizontal2 += str(valor)
        if posicao in [6, 7, 8]:
            horizontal3 += str(valor)
        # vertical
        if posicao in [0, 3, 6]:
            vertical1 += str(valor)
        if posicao in [1, 4, 7]:
            vertical2 += str(valor)
        if posicao in [2, 5, 8]:
            vertical3 += str(valor)
        # diagonal
        if posicao in [0, 4, 8]:
            diagonal1 += str(valor)
        if posicao in [2, 4, 6]:
            diagonal2 += str(valor)
    geral = [horizontal1, horizontal2, horizontal3,
             vertical1, vertical2, vertical3,
             diagonal1, diagonal2]
    for valor in geral:
        conferir_empate += valor
        if valor.isalpha():
            if valor[0] == valor[1] == valor[2]:
                vitoria = True
                simbolo = valor[0]
    if vitoria:
        return f"{simbolo} VENCEU!", "Vitória", simbolo
    elif conferir_empate.isalpha():
        return "Empate"
    else:
        return "Nada"


def sistema_principal(primeiro):
    from time import sleep
    segundo = ""
    if primeiro == "X":
        segundo = "O"
    if primeiro == "O":
        segundo = "X"
    while True:
        global x
        global o
        checar_resposta(f"\n{primeiro} >> ", primeiro)
        verificacao1 = checar_vitoria(lista_de_numeros)
        print()
        if verificacao1[1] == "Vitória":
            print("-" * 30)
            print(f"{verificacao1[0]}".center(30))
            print("-" * 30)
            if verificacao1[2] == "X":
                x += 1
            if verificacao1[2] == "O":
                o += 1
            break
        if verificacao1 == "Empate":
            print("-" * 30)
            print(f"DEU VELHA!".center(30))
            print("-" * 30)
            break
        checar_resposta(f"\n{segundo} >> ", segundo)
        verificacao2 = checar_vitoria(lista_de_numeros)
        print()
        if verificacao2[1] == "Vitória":
            print("-" * 30)
            print(f"{verificacao2[0]}".center(30))
            print("-" * 30)
            if verificacao2[2] == "X":
                x += 1
            if verificacao2[2] == "O":
                o += 1
            break
        if verificacao2 == "Empate":
            print("-" * 30)
            print(f"DEU VELHA!".center(30))
            print("-" * 30)
            break
    sleep(1)
    print()
    print("-" * 30)
    print("Tabela de Pontuação".center(30))
    print("-" * 30)
    print(f"X = {x}\nO = {o}")


def jogo_da_velha():
    while True:
        for adicionar in range(0, 9):
            lista_de_numeros[adicionar] = ' '
        sistema_principal(primeiro_a_jogar())
        while True:
            try:
                print()
                continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
                print()
                if continuar in 'NS':
                    break
            except IndexError:
                print("Digite Algo!")
            else:
                print("Digite um valor válido!")
        if continuar == "N":
            print("Programa Finalizado </>")
            break
        if continuar == "S":
            continue


jogo_da_velha()
