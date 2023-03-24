# Versão do PYTHON: 3.10

# /*******************************************************************************
# Autor: Naila Suele Mascarenhas Silva
# Componente Curricular: Algoritmos I
# Concluido em: 18/05/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# ******************************************************************************************/

import random


# Menu inicial
def menu():
    print("\033[1;34m")
    print("█▀▀ █▀▀█ █▀▄▀█ █▀▀█ █▀▀ 　 █▀▀ █▀▀ █▀▀█ █░░█ █▀▀ █▀▀ ░▀░ █▀▀▄ █▀▀█ █▀▀\n"
          "▀▀█ █░░█ █░▀░█ █▄▄█ ▀▀█ 　 █▀▀ ▀▀█ █░░█ █░░█ █▀▀ █░░ ▀█▀ █░░█ █▄▄█ ▀▀█\n"
          "▀▀▀ ▀▀▀▀ ▀░░░▀ ▀░░▀ ▀▀▀ 　 ▀▀▀ ▀▀▀ ▀▀▀█ ░▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀░ ▀░░▀ ▀▀▀\n")
    print("\033[1;34m─" * 70)
    print(f"{'1. COMEÇAR JOGO' : ^65}\n"
          f"{'2. INSTRUÇÕES' :^63}\n"
          f"{'3. SAIR':^58}"
          "    ")
    print("─" * 70)
    print("\n\033[m", end="")


# Gerador de matrizes, dependendo no nível escolhido.
def level(variation, amount):
    matriz = []
    for linha in range(variation):
        matriz.append([])
        for coluna in range(variation):
            matriz[linha].append("0")
    # lista para armazenar números e evitar repetições.
    lista_numeros = []
    while len(lista_numeros) != amount:
        for linha in range(variation):
            for coluna in range(variation):
                numero = random.randint(1, amount)
                if numero not in lista_numeros:
                    lista_numeros.append(numero)
    pos = 0
    for lin in range(variation):
        for col in range(variation):
            matriz[lin][col] = lista_numeros[pos]
            pos += 1
    return matriz


# Criação da matriz oculta.
def hidden_matrix(variation):
    matriz_oculta1 = []
    for linha in range(variation):
        matriz_oculta1.append([])
        for coluna in range(variation):
            matriz_oculta1[linha].append(0)
    return matriz_oculta1


# Criar lista zerada.
def zeroed_matrix(variation):
    matrix = []
    for qnt in range(variation):
        matrix.append(0)
    return matrix


# Função que retorna a soma dependendo da linha ou da coluna.
def sums(lc, value, matrix):
    soma_0 = soma_1 = soma_2 = soma_3 = soma_4 = 0
    soma_col_0 = soma_col_1 = soma_col_2 = soma_col_3 = soma_col_4 = 0
    if lc == 1:
        if value == 0:
            for linha in matrix[0]:
                soma_0 += linha
            return soma_0
        elif value == 1:
            for linha in matrix[1]:
                soma_1 += linha
            return soma_1
        elif value == 2:
            for linha in matrix[2]:
                soma_2 += linha
            return soma_2
        elif value == 3:
            for linha in matrix[3]:
                soma_3 += linha
            return soma_3
        elif value == 4:
            for linha in matrix[4]:
                soma_4 += linha
            return soma_4

    elif lc == 2:
        if value == 0:
            for linha in range(len(matrix)):
                soma_col_0 += matrix[linha][0]
            return soma_col_0
        elif value == 1:
            for linha in range(len(matrix)):
                soma_col_1 += matrix[linha][1]
            return soma_col_1
        elif value == 2:
            for linha in range(len(matrix)):
                soma_col_2 += matrix[linha][2]
            return soma_col_2
        elif value == 3:
            for linha in range(len(matrix)):
                soma_col_3 += matrix[linha][3]
            return soma_col_3
        elif value == 4:
            for linha in range(len(matrix)):
                soma_col_4 += matrix[linha][4]
            return soma_col_4


# Verificar meior e menor.
def biggest_lower(matrix, linecolumn, number):
    if linecolumn == "1":
        maior = max(matrix[number])
        menor = min(matrix[number])
        return maior, menor


# Verificar maior valor da coluna
def biggest_column(matriz, num_coluna):
    lista_maiores = []
    for linha in range(len(matriz)):
        lista_maiores.append(matriz[linha][num_coluna])
    maior_valor = max(lista_maiores)
    return maior_valor


# Retornar uma lista dos elementos da coluna.
def retornar_lista_col(matriz, num_coluna):
    lista_col = []
    for linha in range(len(matriz)):
        lista_col.append(matriz[linha][num_coluna])
    return lista_col


# Verificar onde o elemento está localizado na matriz.
def local(matriz, num_coluna, maior):
    lista_maiores = []
    for linha in range(len(matriz)):
        lista_maiores.append(matriz[linha][num_coluna])
    localiz = lista_maiores.index(maior)
    return localiz


# Verificar menor elemento da coluna
def minor_list(matriz, num_coluna):
    lista_menores = []
    for linha in range(len(matriz)):
        lista_menores.append(matriz[linha][num_coluna])
    return lista_menores


# Verificar maior elemento da linha.
def biggest_line(matrix, numerolin):
    biggestlist = []
    checklist = []
    for col in range(len(matrix)):
        biggestlist.append(matrix[numerolin][col])
    for c in biggestlist:
        if c != 0:
            checklist.append(c)
    if len(checklist) > 0:
        maior = max(checklist)
        return maior
    elif len(checklist) == 0:
        return 0


# Verificar menor elemento da linha.
def lower_line(matrix, numerolin):
    lowerlist = []
    checklist = []
    for col in range(len(matrix)):
        lowerlist.append(matrix[numerolin][col])
    for c in lowerlist:
        if c != 0:
            checklist.append(c)
    if len(checklist) > 0:
        menor = min(checklist)
        return menor
    elif len(checklist) == 0:
        return 0


# Verificar menor elemento da coluna.
def smallest_column(matriz, numerocol):
    listamenores = []
    lista_verificar = []
    for linha in range(len(matriz)):
        listamenores.append(matriz[linha][numerocol])
    for i in listamenores:
        if i != 0:
            lista_verificar.append(i)
    if len(lista_verificar) > 0:
        menor = min(lista_verificar)
        return menor
    elif len(lista_verificar) == 0:
        return 0


# Verificar onde está localizado o menor.
def local_menor(matriz, num_coluna, maior):
    lista_menores = []
    for linha in range(len(matriz)):
        lista_menores.append(matriz[linha][num_coluna])
    localiz = lista_menores.index(maior)
    return localiz


# Retornar lista com elementos da coluna.
def lista_coluna(matriz, num_coluna):
    lista_col = []
    for linha in range(len(matriz)):
        lista_col.append(matriz[linha][num_coluna])
    return lista_col


# Retornar matriz copiada
def copy_matrix(matriz):
    matrix = []
    for linha in range(len(matriz)):
        matrix.append(matriz[linha])
    return matrix


# Retornar a diferença absoluta entre o valor da soma e o valor do chute.
def evaluate(value, soma):
    dif = value - soma
    return abs(dif)


# Retornar uma matriz idêntica
def identical_matrix(matrizcop, numerolc):
    for linha in matrizcop[numerolc]:
        if linha != 0:
            lugar = matrizcop[numerolc].index(linha)
            matrizcop[numerolc][lugar] = 0
    return matrizcop


# Retornar qual o placar
def scoreboard(matrix):
    if len(matrix) == 3:
        return 3
    elif len(matrix) == 4:
        return 4
    elif len(matrix) == 5:
        return 5


def store_sums_line(matriz):
    sums_line = []
    for linha in range(len(matriz)):
        sum_line = sums(1, linha, matriz)
        sums_line.append(sum_line)
    return sums_line


def store_sums_column(matriz):
    sums_column = []
    for linha in range(len(matriz)):
        sum_line = sums(2, linha, matriz)
        sums_column.append(sum_line)
    return sums_column


# Mostrar a matriz de maneira formatada
def show(matrix, size):
    list_lc = [0, 1, 2, 3, 4]
    list_name = ["LINHA", "COLUNA"]
    if size == 3:
        print("\033[1;34m─" * 50)
        print(" LINHA")
        print("       ┌───────┬──────┬──────┐")
        print(f"   {list_lc[0]:<4}│{matrix[0][0]:^7}│{matrix[0][1]:^6}│{matrix[0][2]:^6}│")
        print("       ├───────┼──────┼──────┤")
        print(f"   {list_lc[1]:<4}│{matrix[1][0]:^7}│{matrix[1][1]:^6}│{matrix[1][2]:^6}│")
        print("       ├───────┼──────┼──────┤")
        print(f"   {list_lc[2]:<4}│{matrix[2][0]:^7}│{matrix[2][1]:^6}│{matrix[2][2]:^6}│")
        print("       └───────┴──────┴──────┘")
        print(f" {list_name[1]:<6}{list_lc[0]:^8}{list_lc[1]:^8}{list_lc[2]:^8}")
        print("─" * 50)
        print("\n\033[m", end="")

    elif size == 4:
        print("\033[1;34m─" * 50)
        print(" LINHA")
        print("       ┌──────┬──────┬──────┬──────┐")
        print(f"   {list_lc[0]:<4}│{matrix[0][0]:^6}│{matrix[0][1]:^6}│{matrix[0][2]:^6}│{matrix[0][3]:^6}│")
        print("       ├──────┼──────┼──────┼──────┤")
        print(f"   {list_lc[1]:<4}│{matrix[1][0]:^6}│{matrix[1][1]:^6}│{matrix[1][2]:^6}│{matrix[1][3]:^6}│")
        print("       ├──────┼──────┼──────┼──────┤")
        print(f"   {list_lc[2]:<4}│{matrix[2][0]:^6}│{matrix[2][1]:^6}│{matrix[2][2]:^6}│{matrix[2][3]:^6}│")
        print("       ├──────┼──────┼──────┼──────┤")
        print(f"   {list_lc[3]:<4}│{matrix[3][0]:^6}│{matrix[3][1]:^6}│{matrix[3][2]:^6}│{matrix[3][3]:^6}│")
        print("       └──────┴──────┴──────┴──────┘")
        print(f" {list_name[1]:<6}{list_lc[0]:^8}{list_lc[1]:^8}{list_lc[2]:^8}{list_lc[3]:^6}")
        print("─" * 50)
        print("\n\033[m", end="")
    elif size == 5:
        print("\033[1;34m─" * 50)
        print(" LINHA")
        print("       ┌──────┬──────┬──────┬──────┬──────┐")
        print(
            f"   {list_lc[0]:<4}│{matrix[0][0]:^6}│{matrix[0][1]:^6}│{matrix[0][2]:^6}│{matrix[0][3]:^6}│{matrix[0][4]:^6}│")
        print("       ├──────┼──────┼──────┼──────┼──────┤")
        print(
            f"   {list_lc[1]:<4}│{matrix[1][0]:^6}│{matrix[1][1]:^6}│{matrix[1][2]:^6}│{matrix[1][3]:^6}│{matrix[1][4]:^6}│")
        print("       ├──────┼──────┼──────┼──────┼──────┤")
        print(
            f"   {list_lc[2]:<4}│{matrix[2][0]:^6}│{matrix[2][1]:^6}│{matrix[2][2]:^6}│{matrix[2][3]:^6}│{matrix[2][4]:^6}│")
        print("       ├──────┼──────┼──────┼──────┼──────┤")
        print(
            f"   {list_lc[3]:<4}│{matrix[3][0]:^6}│{matrix[3][1]:^6}│{matrix[3][2]:^6}│{matrix[3][3]:^6}│{matrix[3][4]:^6}│")
        print("       ├──────┼──────┼──────┼──────┼──────┤")
        print(
            f"   {list_lc[4]:<4}│{matrix[4][0]:^6}│{matrix[4][1]:^6}│{matrix[4][2]:^6}│{matrix[4][3]:^6}│{matrix[4][4]:^6}│")
        print("       └──────┴──────┴──────┴──────┴──────┘")
        print(f" {list_name[1]:<6}{list_lc[0]:^8}{list_lc[1]:^8}{list_lc[2]:^8}{list_lc[3]:^6}{list_lc[4]:^6}")
        print("─" * 50)
        print("\n\033[m", end="")


# Mostrar o placar.
def players_score(players, score1, score2):
    print("\033[1;34m─" * 30)
    print("─" * 10, "PLACAR", "─" * 12)
    print("─" * 30)
    print(f"─" * 10, f"{players[0]:^6}", "─" * 12)
    print("┌────────────────┬──────┐")
    print(f"│{players[0]:^16}│{score1:^6}│")
    print("└────────────────┴──────┘")
    print(f"─" * 10, f"{players[1]:^6}", "─" * 12)
    print("┌────────────────┬──────┐")
    print(f"│{players[1]:^16}│{score2 :^6}│")
    print("└────────────────┴──────┘")
    print("─" * 30)
    print("\n\033[m", end="")


# Mostrar o histórico.
def historic(players, historicp1, historicp2):
    print("\033[1;34m")
    print("┌────────────────┬───────────┐")
    print(f"│   HISTÓRICO    │{players[0] :^11}│")
    print("└────────────────┴───────────┘")
    print("    CHUTE           SITUAÇÃO ")
    print("─" * 30)
    for k, v in historicp1.items():
        print(f"{k:^12}       {v:^12}")
        print("─" * 30)
    print("┌────────────────┬───────────┐")
    print(f"│   HISTÓRICO    │{players[1] :^11}│")
    print("└────────────────┴───────────┘")
    print("    CHUTE           SITUAÇÃO ")
    print("─" * 30)
    for k, v in historicp2.items():
        print(f"{k:^12}       {v:^12}")
        print("─" * 30)
    print("\n\033[m", end="")


def winner(scorep1, scorep2, players):
    if scorep1 > scorep2:
        print("\033[1;34m")
        print("─" * 30)
        print(f"     {players[0]} GANHOU A PARTIDA!   ")
        print("─" * 30)
        print("\n\033[m", end="")
    elif scorep2 > scorep1:
        print("\033[1;34m")
        print("─" * 30)
        print(f"     {players[1]} GANHOU A PARTIDA!   ")
        print("─" * 30)
        print("\n\033[m", end="")
    elif scorep1 == scorep2:
        print("\033[1;34m")
        print("─" * 50)
        print(f"    EMPATE!!! {players[0]} e {players[1]} GANHARAM A PARTIDA!  ")
        print("─" * 50)
        print("\n\033[m", end="")


def number_side(matriz):
    if len(matriz) == 3:
        print("[0]   [1]   [2]")
    elif len(matriz) == 4:
        print("[0]   [1]   [2]   [3]")
    elif len(matriz) == 5:
        print("[0]   [1]   [2]   [3]   [4]")


def instructions():
    print("\033[1;34m")
    print("░█▀▄▀█ ─█▀▀█ ░█▄─░█ ░█─░█ ─█▀▀█ ░█     ░█▀▀▄ ░█▀▀▀ 　 ░█─░█ ░█▀▀▀█ ░█▀▀▀█\n"
          "░█░█░█ ░█▄▄█ ░█░█░█ ░█─░█ ░█▄▄█ ░█     ░█─░█ ░█▀▀▀ 　 ░█─░█ ─▀▀▀▄▄ ░█──░█\n"
          "░█──░█ ░█─░█ ░█──▀█ ─▀▄▄▀ ░█─░█ ░█▄▄█  ░█▄▄▀ ░█▄▄▄ 　 ─▀▄▄▀ ░█▄▄▄█ ░█▄▄▄█\n")
    print("ATENÇÃO:\n")
    print("1. Se a coluna ou a linha estiver completa e você tentar chutar a soma dela,"
          "você perde a chance!\n"
          "2. Quando o jogo pedir o nome dos jogadores, apenas letras são aceitas!\n"
          "3. Apenas valores válidos devem ser digitados nas entradas.\n")
    print("SOBRE O JOGO:\n")
    print("─> O tabuleiro inicial é composto por zeros.\n"
          "─> A principal missão no jogo é tentar acertar a soma da coluna ou da linha escolhida.\n"
          "─> O jogador que chegar mais próximo do valor da soma ganha a rodada e aumenta seu placar.\n"
          "─> Se o valor que o jogador chutar for maior do que a soma verdadeira é liberado o elemento com MAIOR\n"
          "valor da linha ou da coluna.\n"
          "─> Se o valor que o jogador chutar for menor do que a soma verdadeira é liberado o elemento com MENOR\n"
          "valor da linha ou da coluna. \n"
          "─> Se o jogador acertar justamente a soma verdadeira é liberado todos os elementos que compõem a linha\n"
          "ou a coluna.\n"
          "─> Se os jogadores que estão jogando no mesmo tabuleiro chutarem o mesmo valor na mesma linha ou coluna\n"
          "será liberado apenas o valor que condiz ao chute! ")

    print("\n\033[m", end="")


def show_sums(matrix, size, sums_line, sums_colunm):
    list_name = ["LINHA", "COLUNA"]

    if size == 3:
        print("\033[1;34m─" * 50)
        print(f"{'SOMAS REVELADAS':^50}")
        print("─" * 50)
        print(" LINHA")
        print("       ┌───────┬──────┬──────┐")
        print(f"   {sums_line[0]:<4}│{matrix[0][0]:^7}│{matrix[0][1]:^6}│{matrix[0][2]:^6}│")
        print("       ├───────┼──────┼──────┤")
        print(f"   {sums_line[1]:<4}│{matrix[1][0]:^7}│{matrix[1][1]:^6}│{matrix[1][2]:^6}│")
        print("       ├───────┼──────┼──────┤")
        print(f"   {sums_line[2]:<4}│{matrix[2][0]:^7}│{matrix[2][1]:^6}│{matrix[2][2]:^6}│")
        print("       └───────┴──────┴──────┘")
        print(f" {list_name[1]:<6}{sums_colunm[0]:^8}{sums_colunm[1]:^8}{sums_colunm[2]:^8}")
        print("─" * 50)
        print("\n\033[m", end="")

    elif size == 4:
        print("\033[1;34m─" * 50)
        print(f"{'SOMAS REVELADAS':^50}")
        print("─" * 50)
        print(" LINHA")
        print("       ┌──────┬──────┬──────┬──────┐")
        print(f"   {sums_line[0]:<4}│{matrix[0][0]:^6}│{matrix[0][1]:^6}│{matrix[0][2]:^6}│{matrix[0][3]:^6}│")
        print("       ├──────┼──────┼──────┼──────┤")
        print(f"   {sums_line[1]:<4}│{matrix[1][0]:^6}│{matrix[1][1]:^6}│{matrix[1][2]:^6}│{matrix[1][3]:^6}│")
        print("       ├──────┼──────┼──────┼──────┤")
        print(f"   {sums_line[2]:<4}│{matrix[2][0]:^6}│{matrix[2][1]:^6}│{matrix[2][2]:^6}│{matrix[2][3]:^6}│")
        print("       ├──────┼──────┼──────┼──────┤")
        print(f"   {sums_line[3]:<4}│{matrix[3][0]:^6}│{matrix[3][1]:^6}│{matrix[3][2]:^6}│{matrix[3][3]:^6}│")
        print("       └──────┴──────┴──────┴──────┘")
        print(f" {list_name[1]:<6}{sums_colunm[0]:^8}{sums_colunm[1]:^8}{sums_colunm[2]:^8}{sums_colunm[3]:^6}")
        print("─" * 50)
        print("\n\033[m", end="")
    elif size == 5:
        print("\033[1;34m─" * 50)
        print(f"{'SOMAS REVELADAS':^50}")
        print("─" * 50)
        print(" LINHA")
        print("       ┌──────┬──────┬──────┬──────┬──────┐")
        print(
            f"   {sums_line[0]:<4}│{matrix[0][0]:^6}│{matrix[0][1]:^6}│{matrix[0][2]:^6}│{matrix[0][3]:^6}│{matrix[0][4]:^6}│")
        print("       ├──────┼──────┼──────┼──────┼──────┤")
        print(
            f"   {sums_line[1]:<4}│{matrix[1][0]:^6}│{matrix[1][1]:^6}│{matrix[1][2]:^6}│{matrix[1][3]:^6}│{matrix[1][4]:^6}│")
        print("       ├──────┼──────┼──────┼──────┼──────┤")
        print(
            f"   {sums_line[2]:<4}│{matrix[2][0]:^6}│{matrix[2][1]:^6}│{matrix[2][2]:^6}│{matrix[2][3]:^6}│{matrix[2][4]:^6}│")
        print("       ├──────┼──────┼──────┼──────┼──────┤")
        print(
            f"   {sums_line[3]:<4}│{matrix[3][0]:^6}│{matrix[3][1]:^6}│{matrix[3][2]:^6}│{matrix[3][3]:^6}│{matrix[3][4]:^6}│")
        print("       ├──────┼──────┼──────┼──────┼──────┤")
        print(
            f"   {sums_line[4]:<4}│{matrix[4][0]:^6}│{matrix[4][1]:^6}│{matrix[4][2]:^6}│{matrix[4][3]:^6}│{matrix[4][4]:^6}│")
        print("       └──────┴──────┴──────┴──────┴──────┘")
        print(
            f" {list_name[1]:<6}{sums_colunm[0]:^8}{sums_colunm[1]:^8}{sums_colunm[2]:^8}{sums_colunm[3]:^6}{sums_colunm[4]:^6}")
        print("─" * 50)
        print("\n\033[m", end="")
