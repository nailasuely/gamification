# Versão do PYTHON: 3.10

# /*******************************************************************************
# Autor: Naila
# Componente Curricular: Algoritmos I
# Concluido em: 18/05/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# ******************************************************************************************/

import mod


# Função para um tabuleiro
def board_one(
        matrix, hidden_array, copied_array, players, amount, rounds):
    # Váriaveis para contabilizar o placar.
    score_p1 = 0
    score_p2 = 0

    # Dicionário para armazenar histórico.
    historicP1 = {}
    historicP2 = {}

    # Listas para armazenas todas as somas:
    all_sums_line = mod.store_sums_line(matrix)
    all_sums_column = mod.store_sums_column(matrix)

    while rounds != amount:

        # Caso o usúario queira visualizar as somas e a matriz principal com todos os elementos revelados.
        while not (viewSums := input(f"\nATENÇÃO!\n"
                                     f"\nVOCÊ DESEJA VISUALIZAR TODAS SOMAS? \n"
                                     " [1]  SIM  \n"
                                     " [2]  NÃO \n")).isdigit() or \
                (viewSums := int(viewSums)) < 1 or viewSums > 2:
            print("Digite uma entrada válida\n")
        if viewSums == 1:
            mod.show_sums(matrix, len(matrix), all_sums_line, all_sums_column)

        # Criação da váriavel específica e verificação do valor digitado.
        while not (linecolumn := input(f"{players[0]}: Você escolhe linha ou coluna?\n"
                                       " [1]  LINHA  \n"
                                       " [2]  COLUNA \n")).isdigit() or \
                (linecolumn := int(linecolumn)) < 1 or linecolumn > 2:
            print("Digite uma entrada válida\n")

        # Mostrar para os números das linhas e das colunas.
        mod.show(hidden_array, len(matrix))
        print()
        mod.number_side(matrix)

        while not (lc_number := input("Escolha um número dentre os apresentados ao lado do tabuleiro: ")).isdigit() or \
                (lc_number := int(lc_number)) < 0 or lc_number > len(matrix) - 1:
            print("Digite uma entrada válida\n")

        while not (sum_player1 := input("Qual soma da linha ou coluna que você escolheu? ")).isdigit() or \
                (sum_player1 := int(sum_player1)) < 0:
            print("Digite uma entrada válida\n")

        while not (linecolumn_p2 := input(f"{players[1]}: Você escolhe linha ou coluna?\n"
                                          " [1]  LINHA  \n"
                                          " [2]  COLUNA \n")).isdigit() or \
                (linecolumn_p2 := int(linecolumn_p2)) < 1 or linecolumn_p2 > 2:
            print("Digite uma entrada válida\n")

        mod.show(hidden_array, len(matrix))
        print()
        mod.number_side(matrix)
        while not (
                lc_number_p2 := input(f"Escolha um número dentre os apresentados ao lado do tabuleiro: ")).isdigit() or \
                (lc_number_p2 := int(lc_number_p2)) < 0 or lc_number_p2 > len(matrix) - 1:
            print("Digite uma entrada válida\n")

        while not (sum_player2 := input("Qual soma da linha ou coluna que você escolheu? ")).isdigit() or \
                (sum_player2 := int(sum_player2)) < 0:
            print("Digite uma entrada válida\n")

        # Chamada da função para verificar a soma pertencente a coluna ou a linha dos jogadores.
        sum_value_p1 = mod.sums(linecolumn, lc_number, matrix)
        sum_value_p2 = mod.sums(linecolumn_p2, lc_number_p2, matrix)

        # Variáveis para armazenar o maior e menor valor da linha.
        bigger_row = max(copied_array[lc_number])
        lower_row = mod.lower_line(copied_array, lc_number)
        bigger_row_p2 = max(copied_array[lc_number_p2])
        lower_row_p2 = mod.lower_line(copied_array, lc_number_p2)

        # Verificar se a diferença do jogador 1 é maior que a diferença do jogadoe 2.
        if mod.evaluate(sum_value_p1, sum_player1) < mod.evaluate(sum_value_p2, sum_player2):

            # Verificar se o chute é maior que a soma verdadeira.
            if sum_player1 > sum_value_p1:
                # Armazenar o valor no histórico.
                historicP1[sum_player1] = "Maior"
                # Se a escolha for LINHA.
                if linecolumn == 1:
                    # Procurar localização do maior valor.
                    biggestrow = copied_array[lc_number].index(bigger_row)
                    # Se o local ainda não tiver sido substituído por zero.
                    if copied_array[lc_number][biggestrow] != 0:
                        # Aumenta placar para o jogador 1.
                        score_p1 += 1
                        # Mostrar valor que foi liberado na matriz oculta.
                        hidden_array[lc_number][biggestrow] = bigger_row
                        # Mudar o número que já foi liberado para zero na matriz copiada, para ele não afetar mais o jogo.
                        copied_array[lc_number][biggestrow] = 0
                    else:
                        print("\nLINHA COMPLETA\n")

                    mod.show(hidden_array, len(matrix))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                # Se o jogador escolher COLUNA.
                elif linecolumn == 2:
                    # Procurar o maior valor na coluna.
                    biggest_column = mod.biggest_column(copied_array, lc_number)
                    # Procurar a localização do maior valor.
                    localization = mod.local(copied_array, lc_number, biggest_column)
                    # Se o valor ainda não tiver sido substituído por zero.
                    if copied_array[localization][lc_number] != 0:
                        score_p1 += 1
                        # Liberar o valor na matriz oculta.
                        hidden_array[localization][lc_number] = biggest_column
                        # Substituir o valor por zero na matriz copiada.
                        copied_array[localization][lc_number] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")

                    # Mostrar matriz oculta com valor liberado.
                    mod.show(hidden_array, len(matrix))
                    # Mostrar placar.
                    mod.players_score(players, score_p1, score_p2)
                    # Mostrar histórico.
                    mod.historic(players, historicP1, historicP2)

            # Verificar se o chute é MENOR que a soma verdadeira.
            elif sum_player1 < sum_value_p1:
                historicP1[sum_player1] = "Menor"
                # Se o jogador escolher LINHA.
                if linecolumn == 1:
                    lowerline = copied_array[lc_number].index(lower_row)
                    if copied_array[lc_number][lowerline] != 0:
                        score_p1 += 1
                        hidden_array[lc_number][lowerline] = lower_row
                        copied_array[lc_number][lowerline] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array, len(matrix))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                # Se o jogador escolher coluna.
                elif linecolumn == 2:
                    lowercolumn = mod.smallest_column(copied_array, lc_number)
                    localization = mod.local(copied_array, lc_number, lowercolumn)
                    if copied_array[localization][lc_number] != 0:
                        score_p1 += 1
                        hidden_array[localization][lc_number] = lowercolumn
                        copied_array[localization][lc_number] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")
                    mod.show(hidden_array, len(matrix))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

            # Verificar se o chute é IGUAL à soma verdadeira.
            elif sum_player1 == sum_value_p1:
                # Adiconar chute no histórico.
                historicP1[sum_player1] = "Igual"
                # Se a escolha for linha.
                if linecolumn == 1:
                    # Criação da váriavel.
                    sum_row = 0
                    # Percorrer a linha.
                    for coluna in range(len(matrix)):
                        # Somar valores da linha.
                        sum_row += copied_array[lc_number][coluna]
                    # Se a soma for diferente de zero.
                    if sum_row != 0:
                        # Criação da lista para adicionar números disponíveis da linha.
                        numbers = []
                        # Percorrer matriz copiada.
                        for lin in copied_array[lc_number]:
                            # Se o elemento da linha for diferente de zero.
                            if lin != 0:
                                # Adicionar elemento na lista.
                                numbers.append(lin)
                        # Aumenta placar considerando apenas os números que foram liberados na matriz oculta.
                        score_p1 += len(numbers)
                        # Lista com elementos liberados.
                        number_list = [matrix[lc_number]]
                        # Liberar elementos na matriz oculta.
                        hidden_array[lc_number] = number_list[0]
                        # Percorrer a linha da matriz principal.
                        for line in matrix[lc_number]:
                            # Descobrir localização dos elementos.
                            lugar = matrix[lc_number].index(line)
                            # Trocar valores por zero na matriz copiada.
                            copied_array[lc_number][lugar] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array, len(matrix))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn == 2:
                    lista_coluna = mod.lista_coluna(matrix, lc_number)
                    lista0 = mod.zeroed_matrix(len(matrix))
                    soma = 0
                    for line in range(len(matrix)):
                        hidden_array[line][lc_number] = lista_coluna[line]
                    for lin in range(len(matrix)):
                        soma += copied_array[lin][lc_number]
                    if soma != 0:
                        list_column = []
                        column_elements = mod.retornar_lista_col(copied_array, lc_number)
                        for c in column_elements:
                            if c != 0:
                                list_column.append(c)
                        score_p1 += len(list_column)
                        for line in range(len(matrix)):
                            copied_array[line][lc_number] = lista0[line]
                    else:
                        print("\nCOLUNA COMPLETA\n")
                    mod.show(hidden_array, len(matrix))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

        # Caso a diferença da soma do jogador 2 seja menor
        elif mod.evaluate(sum_value_p1, sum_player1) > mod.evaluate(sum_value_p2, sum_player2):

            # Verificar se o chute é MAIOR que a soma verdadeira.
            if sum_player2 > sum_value_p2:
                historicP2[sum_player2] = "Maior"
                if linecolumn_p2 == 1:
                    biggestrow = copied_array[lc_number_p2].index(bigger_row_p2)
                    if copied_array[lc_number_p2][biggestrow] != 0:
                        score_p2 += 1
                        hidden_array[lc_number_p2][biggestrow] = bigger_row_p2
                        copied_array[lc_number_p2][biggestrow] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array, len(matrix))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn_p2 == 2:
                    biggest_column = mod.biggest_column(copied_array, lc_number_p2)
                    localization = mod.local(copied_array, lc_number_p2, biggest_column)
                    if copied_array[localization][lc_number_p2] != 0:
                        score_p2 += 1
                        hidden_array[localization][lc_number_p2] = biggest_column
                        copied_array[localization][lc_number_p2] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")
                    mod.show(hidden_array, len(matrix))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

            # Verificar se o chute é MENOR que a soma verdadeira.
            elif sum_player2 < sum_value_p2:
                historicP2[sum_player2] = "Menor"
                if linecolumn_p2 == 1:
                    menor_linha_j2 = copied_array[lc_number_p2].index(lower_row_p2)
                    if copied_array[lc_number_p2][menor_linha_j2] != 0:
                        score_p2 += 1
                        hidden_array[lc_number_p2][menor_linha_j2] = lower_row_p2
                        copied_array[lc_number_p2][menor_linha_j2] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array, len(matrix))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn_p2 == 2:
                    menor_coluna_j2 = mod.smallest_column(copied_array, lc_number_p2)
                    localization = mod.local(copied_array, lc_number_p2, menor_coluna_j2)
                    if copied_array[localization][lc_number_p2] != 0:
                        score_p2 += 1
                        hidden_array[localization][lc_number_p2] = menor_coluna_j2
                        copied_array[localization][lc_number_p2] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")
                    mod.show(hidden_array, len(matrix))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

            # Verificar se o chute é IGUAL à soma verdadeira.
            elif sum_player2 == sum_value_p2:
                historicP2[sum_player2] = "Igual"
                if linecolumn_p2 == 1:
                    soma_lin_j2 = 0
                    for coluna in range(len(matrix)):
                        soma_lin_j2 += copied_array[lc_number_p2][coluna]
                    if soma_lin_j2 != 0:
                        listaj2 = []
                        for lin in copied_array[lc_number_p2]:
                            if lin != 0:
                                listaj2.append(lin)
                        score_p2 += len(listaj2)
                        number_list = [matrix[lc_number_p2]]
                        hidden_array[lc_number_p2] = number_list[0]
                        for line in matrix[lc_number_p2]:
                            lugar = matrix[lc_number_p2].index(line)
                            copied_array[lc_number_p2][lugar] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array, len(matrix))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn_p2 == 2:
                    lista_coluna_j2 = mod.lista_coluna(matrix, lc_number_p2)
                    lista0 = mod.zeroed_matrix(len(matrix))
                    sum_player2 = 0
                    for line in range(len(matrix)):
                        hidden_array[line][lc_number_p2] = lista_coluna_j2[line]
                    for lin in range(len(matrix)):
                        sum_player2 += copied_array[lin][lc_number_p2]
                    if sum_player2 != 0:
                        lista_c_j2 = []
                        column_elements = mod.retornar_lista_col(copied_array, lc_number_p2)
                        for c in column_elements:
                            if c != 0:
                                lista_c_j2.append(c)
                        score_p2 += len(lista_c_j2)
                        for line in range(len(matrix)):
                            copied_array[line][lc_number_p2] = lista0[line]
                    else:
                        print("\nCOLUNA COMPLETA\n")
                    mod.show(hidden_array, len(matrix))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

        # caso a diferença seja IGUAL.
        if mod.evaluate(sum_value_p1, sum_player1) == mod.evaluate(sum_value_p2, sum_player2):

            # Se a soma da linha ou coluna é a mesma para os dois jogadores.
            if sum_player1 == sum_player2 and linecolumn == linecolumn_p2:
                if sum_player1 > sum_value_p1:
                    # Adicionar valores chutados no histórico.
                    historicP1[sum_player1] = "Maior"
                    historicP2[sum_player2] = "Maior"
                    if linecolumn == 1:
                        # Descobrir localização do maior número da linha.
                        biggestrow = copied_array[lc_number].index(bigger_row)
                        # Se o elemento for diferente de zero.
                        if copied_array[lc_number][biggestrow] != 0:
                            # Aumenta placar para os dois jogadores.
                            score_p1 += 1
                            score_p2 += 1
                            # Revela elemento na matriz oculta.
                            hidden_array[lc_number][biggestrow] = bigger_row
                            # Troca o elemento por zero na matriz copiada.
                            copied_array[lc_number][biggestrow] = 0
                        else:
                            print("\nLINHA COMPLETA\n")
                        # Mostra matriz oculta.
                        mod.show(hidden_array, len(matrix))
                        # Placar.
                        mod.players_score(players, score_p1, score_p2)
                        # Histórico.
                        mod.historic(players, historicP1, historicP2)

                    # Se a escolha for coluna.
                    elif linecolumn == 2:
                        # Descobrir maior valor na coluna.
                        biggest_column = mod.biggest_column(copied_array, lc_number)
                        # Descobrir qual a localização do maior valor.
                        localization = mod.local(copied_array, lc_number, biggest_column)
                        # Se o elemento for diferente de zero.
                        if copied_array[localization][lc_number] != 0:
                            # Aumenta placar para os dois.
                            score_p1 += 1
                            score_p2 += 1
                            # Libera elemento na matriz oculta.
                            hidden_array[localization][lc_number] = biggest_column
                            # Trocar valor do elemento para zero na matriz copiada.
                            copied_array[localization][lc_number] = 0
                        else:
                            print("\n COLUNA COMPLETA\n")
                        mod.show(hidden_array, len(matrix))
                        mod.players_score(players, score_p1, score_p2)
                        mod.historic(players, historicP1, historicP2)

                elif sum_player1 < sum_value_p1:
                    historicP1[sum_player1] = "Menor"
                    historicP2[sum_player2] = "Menor"
                    if linecolumn == 1:
                        lowerline = copied_array[lc_number].index(lower_row)
                        if copied_array[lc_number][lowerline] != 0:
                            score_p1 += 1
                            score_p2 += 1
                            hidden_array[lc_number][lowerline] = lower_row
                            copied_array[lc_number][lowerline] = 0
                        else:
                            print("\nLINHA COMPLETA\n")
                        mod.show(hidden_array, len(matrix))
                        mod.players_score(players, score_p1, score_p2)
                        mod.historic(players, historicP1, historicP2)

                    elif linecolumn == 2:
                        lowercolumn = mod.smallest_column(copied_array, lc_number)
                        localization = mod.local(copied_array, lc_number, lowercolumn)
                        if copied_array[localization][lc_number] != 0:
                            score_p1 += 1
                            score_p2 += 1
                            hidden_array[localization][lc_number] = lowercolumn
                            copied_array[localization][lc_number] = 0
                        else:
                            print("\n COLUNA COMPLETA\n")
                        mod.show(hidden_array, len(matrix))
                        mod.players_score(players, score_p1, score_p2)
                        mod.historic(players, historicP1, historicP2)

                elif sum_player1 == sum_value_p1:
                    historicP1[sum_player1] = "Igual"
                    historicP2[sum_player2] = "Igual"
                    if linecolumn == 1:
                        sum_row = 0
                        for coluna in range(len(matrix)):
                            sum_row += copied_array[lc_number][coluna]
                        if sum_row != 0:
                            numbers = []
                            for lin in copied_array[lc_number]:
                                if lin != 0:
                                    numbers.append(lin)
                            score_p1 += len(numbers)
                            score_p2 += len(numbers)
                            number_list = [matrix[lc_number]]
                            hidden_array[lc_number] = number_list[0]
                            for line in matrix[lc_number]:
                                lugar = matrix[lc_number].index(line)
                                copied_array[lc_number][lugar] = 0
                        else:
                            print("\nLINHA COMPLETA\n")
                        mod.show(hidden_array, len(matrix))
                        mod.players_score(players, score_p1, score_p2)
                        mod.historic(players, historicP1, historicP2)

                    elif linecolumn == 2:
                        lista_coluna = mod.lista_coluna(matrix, lc_number)
                        lista0 = mod.zeroed_matrix(len(matrix))
                        soma = 0
                        for line in range(len(matrix)):
                            hidden_array[line][lc_number] = lista_coluna[line]
                        for lin in range(len(matrix)):
                            soma += copied_array[lin][lc_number]
                        if soma != 0:
                            list_column = []
                            column_elements = mod.retornar_lista_col(copied_array, lc_number)
                            for c in column_elements:
                                if c != 0:
                                    list_column.append(c)
                            score_p1 += len(list_column)
                            score_p2 += len(list_column)
                            for line in range(len(matrix)):
                                copied_array[line][lc_number] = lista0[line]
                        else:
                            print("\nCOLUNA COMPLETA\n")
                        mod.show(hidden_array, len(matrix))
                        mod.players_score(players, score_p1, score_p2)
                        mod.historic(players, historicP1, historicP2)

            # Se a diferença absoluta for igual, mas os jogadores escolheram somas diferentes em linha ou coluna diferente.
            else:
                if sum_player1 > sum_value_p1:
                    historicP1[sum_player1] = "Maior"
                    if linecolumn == 1:
                        biggestrow = copied_array[lc_number].index(bigger_row)
                        if copied_array[lc_number][biggestrow] != 0:
                            score_p1 += 1
                            hidden_array[lc_number][biggestrow] = bigger_row
                            copied_array[lc_number][biggestrow] = 0
                        else:
                            print("\nLINHA COMPLETA\n")

                    elif linecolumn == 2:
                        biggest_column = mod.biggest_column(copied_array, lc_number)
                        localization = mod.local(copied_array, lc_number, biggest_column)
                        if copied_array[localization][lc_number] != 0:
                            score_p1 += 1
                            hidden_array[localization][lc_number] = biggest_column
                            copied_array[localization][lc_number] = 0
                        else:
                            print("\n COLUNA COMPLETA\n")

                elif sum_player1 < sum_value_p1:
                    historicP1[sum_player1] = "Menor"
                    if linecolumn == 1:
                        lowerline = copied_array[lc_number].index(lower_row)
                        if copied_array[lc_number][lowerline] != 0:
                            score_p1 += 1
                            hidden_array[lc_number][lowerline] = lower_row
                            copied_array[lc_number][lowerline] = 0
                        else:
                            print("\nLINHA COMPLETA\n")

                    elif linecolumn == 2:
                        lowercolumn = mod.smallest_column(copied_array, lc_number)
                        localization = mod.local(copied_array, lc_number, lowercolumn)
                        if copied_array[localization][lc_number] != 0:
                            score_p1 += 1
                            hidden_array[localization][lc_number] = lowercolumn
                            copied_array[localization][lc_number] = 0
                        else:
                            print("\n COLUNA COMPLETA\n")

                elif sum_player1 == sum_value_p1:
                    historicP1[sum_player1] = "Igual"
                    if linecolumn == 1:
                        sum_row = 0
                        for coluna in range(len(matrix)):
                            sum_row += copied_array[lc_number][coluna]
                        if sum_row != 0:
                            numbers = []
                            for lin in copied_array[lc_number]:
                                if lin != 0:
                                    numbers.append(lin)
                            score_p1 += len(numbers)
                            number_list = [matrix[lc_number]]
                            hidden_array[lc_number] = number_list[0]
                            for line in matrix[lc_number]:
                                lugar = matrix[lc_number].index(line)
                                copied_array[lc_number][lugar] = 0
                        else:
                            print("\nLINHA COMPLETA\n")

                    elif linecolumn == 2:
                        lista_coluna = mod.lista_coluna(matrix, lc_number)
                        lista0 = mod.zeroed_matrix(len(matrix))
                        soma = 0
                        for line in range(len(matrix)):
                            hidden_array[line][lc_number] = lista_coluna[line]
                        for lin in range(len(matrix)):
                            soma += copied_array[lin][lc_number]
                        if soma != 0:
                            list_column = []
                            column_elements = mod.retornar_lista_col(copied_array, lc_number)
                            for c in column_elements:
                                if c != 0:
                                    list_column.append(c)
                            score_p1 += len(list_column)
                            for line in range(len(matrix)):
                                copied_array[line][lc_number] = lista0[line]
                        else:
                            print("\nCOLUNA COMPLETA\n")

                if sum_player2 > sum_value_p2:
                    historicP2[sum_player2] = "Maior"
                    if linecolumn_p2 == 1:
                        bigger_row_p02 = max(copied_array[lc_number_p2])
                        biggestrow2 = copied_array[lc_number_p2].index(bigger_row_p02)
                        if copied_array[lc_number_p2][biggestrow2] != 0:
                            score_p2 += 1
                            hidden_array[lc_number_p2][biggestrow2] = bigger_row_p02
                            copied_array[lc_number_p2][biggestrow2] = 0
                        else:
                            print("\nLINHA COMPLETA\n")
                        mod.show(hidden_array, len(matrix))
                        mod.players_score(players, score_p1, score_p2)
                        mod.historic(players, historicP1, historicP2)

                    elif linecolumn_p2 == 2:
                        biggest_column = mod.biggest_column(copied_array, lc_number_p2)
                        localization = mod.local(copied_array, lc_number_p2, biggest_column)
                        if copied_array[localization][lc_number_p2] != 0:
                            score_p2 += 1
                            hidden_array[localization][lc_number_p2] = biggest_column
                            copied_array[localization][lc_number_p2] = 0
                        else:
                            print("\n COLUNA COMPLETA\n")
                        mod.show(hidden_array, len(matrix))
                        mod.players_score(players, score_p1, score_p2)
                        mod.historic(players, historicP1, historicP2)

                elif sum_player2 < sum_value_p2:
                    historicP2[sum_player2] = "Menor"
                    if linecolumn_p2 == 1:
                        lower_row_p02 = mod.lower_line(copied_array, lc_number_p2)
                        menor_linha_j2 = copied_array[lc_number_p2].index(lower_row_p02)
                        if copied_array[lc_number_p2][menor_linha_j2] != 0:
                            score_p2 += 1
                            hidden_array[lc_number_p2][menor_linha_j2] = lower_row_p02
                            copied_array[lc_number_p2][menor_linha_j2] = 0
                        else:
                            print("\nLINHA COMPLETA\n")
                        mod.show(hidden_array, len(matrix))
                        mod.players_score(players, score_p1, score_p2)
                        mod.historic(players, historicP1, historicP2)

                    elif linecolumn_p2 == 2:
                        menor_coluna_j2 = mod.smallest_column(copied_array, lc_number_p2)
                        localization = mod.local(copied_array, lc_number_p2, menor_coluna_j2)
                        if copied_array[localization][lc_number_p2] != 0:
                            score_p2 += 1
                            hidden_array[localization][lc_number_p2] = menor_coluna_j2
                            copied_array[localization][lc_number_p2] = 0
                        else:
                            print("\n COLUNA COMPLETA\n")
                        mod.show(hidden_array, len(matrix))
                        mod.players_score(players, score_p1, score_p2)
                        mod.historic(players, historicP1, historicP2)

                elif sum_player2 == sum_value_p2:
                    historicP2[sum_player2] = "Igual"
                    if linecolumn_p2 == 1:
                        soma_lin_j2 = 0
                        for coluna in range(len(matrix)):
                            soma_lin_j2 += copied_array[lc_number_p2][coluna]
                        if soma_lin_j2 != 0:
                            listaj2 = []
                            for lin in copied_array[lc_number_p2]:
                                if lin != 0:
                                    listaj2.append(lin)
                            score_p2 += len(listaj2)
                            number_list = [matrix[lc_number_p2]]
                            hidden_array[lc_number_p2] = number_list[0]
                            for line in matrix[lc_number_p2]:
                                lugar = matrix[lc_number_p2].index(line)
                                copied_array[lc_number_p2][lugar] = 0
                        else:
                            print("\nLINHA COMPLETA\n")
                        mod.show(hidden_array, len(matrix))
                        mod.players_score(players, score_p1, score_p2)
                        mod.historic(players, historicP1, historicP2)

                    elif linecolumn_p2 == 2:
                        lista_coluna_j2 = mod.lista_coluna(matrix, lc_number_p2)
                        lista0 = mod.zeroed_matrix(len(matrix))
                        sum_player2 = 0
                        for line in range(len(matrix)):
                            hidden_array[line][lc_number_p2] = lista_coluna_j2[line]
                        for lin in range(len(matrix)):
                            sum_player2 += copied_array[lin][lc_number_p2]
                        if sum_player2 != 0:
                            lista_c_j2 = []
                            column_elements = mod.retornar_lista_col(copied_array, lc_number_p2)
                            for c in column_elements:
                                if c != 0:
                                    lista_c_j2.append(c)
                            score_p2 += len(lista_c_j2)
                            for line in range(len(matrix)):
                                copied_array[line][lc_number_p2] = lista0[line]
                        else:
                            print("\nCOLUNA COMPLETA\n")
                        mod.show(hidden_array, len(matrix))
                        mod.players_score(players, score_p1, score_p2)
                        mod.historic(players, historicP1, historicP2)

        # Se o valor que a função recebeu para "rounds" foi negativa, significa que os jogadores escolheram
        # finalizar a partida com tabuleiro completo.
        if rounds == -2:
            # Verifica se o tabuleiro na matriz oculta já foi completo.
            if matrix == hidden_array:
                # Se sim, ele finaliza a partida.
                rounds = -1
        # Se o valor que a função recebeu for positiva, significa que a partida irá acabar pelo número de rodadas.
        elif rounds >= 0:
            # Aumenta as rodadas até chegar na quantidade de rodadas que os jogadores escolheram.
            rounds += 1
            # Se o tabuleiro ficar completo antes das rodadas acabarem.
            if matrix == hidden_array:
                rounds = -1
                amount = -1
                print("\033[1;34m─" * 30)
                print("\n     TABULEIRO COMPLETO!\n")
                print("─" * 30)
                print("\n\033[m", end="")

    # Mostra quem ganhou o jogo.
    mod.winner(score_p1, score_p2, players)
    print()
    mod.show_sums(matrix, len(matrix), all_sums_line, all_sums_column)


# Função para jogo com dois tabuleiros.
def two_boards(
        matrix_p1, matrix_j2,
        hidden_array_p1, hidden_array_p2,
        copied_array_p1, copied_array_p2,
        players, amount, rounds):

    # Variavéis para armazenar placar.
    score_p1 = 0
    score_p2 = 0

    # Dicionário para armazenar histórico.
    historicP1 = {}
    historicP2 = {}

    # Armazenar todas as somas das linhas do jogador 1.
    all_sums_line = mod.store_sums_line(matrix_p1)
    # Armazenar todas as somas das colunas do jogador dois.
    all_sums_column = mod.store_sums_column(matrix_p1)
    # Armazenar todas as somas das linhas do jogador 2.
    all_sums_line_p2 = mod.store_sums_line(matrix_j2)
    # Armazenar todas as somas das colunas do jogador 2.
    all_sums_column_p2 = mod.store_sums_column(matrix_j2)

    while rounds < amount:

        # Caso o usúario queira visualizar as somas e a matriz principal com todos os elementos revelados.
        while not (viewSums := input(f"\nATENÇÃO!\n"
                                     f"VOCÊ DESEJA VISUALIZAR TODAS SOMAS ANTES DE INCIAR O JOGO?\n"
                                     " [1]  SIM  \n"
                                     " [2]  NÃO \n")).isdigit() or \
                (viewSums := int(viewSums)) < 1 or viewSums > 2:
            print("Digite uma entrada válida\n")
        if viewSums == 1:
            # Se sim, será mostrado a matriz principal com as somas.
            mod.show_sums(matrix_p1, len(matrix_p1), all_sums_line, all_sums_column)
            print()
            mod.show_sums(matrix_j2, len(matrix_j2), all_sums_line_p2, all_sums_column_p2)

        # Criação da váriavel específica e verificação do valor digitado.
        while not (linecolumn := input(f"{players[0]}: Você escolhe linha ou coluna?\n"
                                       " [1]  LINHA  \n"
                                       " [2]  COLUNA \n")).isdigit() or \
                (linecolumn := int(linecolumn)) < 1 or linecolumn > 2:
            print("Digite uma entrada válida\n")

        mod.show(hidden_array_p1, len(matrix_p1))
        print()
        mod.number_side(matrix_p1)
        while not (lc_number := input("Escolha um número dentre os apresentados ao lado do tabuleiro: ")).isdigit() or \
                (lc_number := int(lc_number)) < 0 or lc_number > len(matrix_p1) - 1:
            print("Digite uma entrada válida\n")

        while not (sum_player1 := input("Qual soma da linha ou coluna que você escolheu? ")).isdigit() or \
                (sum_player1 := int(sum_player1)) < 0:
            print("Digite uma entrada válida\n")

        while not (linecolumn_p2 := input(f"{players[1]}: Você escolhe linha ou coluna?\n"
                                          " [1]  LINHA  \n"
                                          " [2]  COLUNA \n")).isdigit() or \
                (linecolumn_p2 := int(linecolumn_p2)) < 1 or linecolumn_p2 > 2:
            print("Digite uma entrada válida\n")

        mod.show(hidden_array_p2, len(matrix_j2))
        print()
        mod.number_side(matrix_j2)
        while not (
                lc_number_p2 := input("Escolha um número dentre os apresentados ao lado do tabuleiro: ")).isdigit() or \
                (lc_number_p2 := int(lc_number_p2)) < 0 or lc_number_p2 > len(matrix_j2) - 1:
            print("Digite uma entrada válida\n")

        while not (sum_player2 := input("Qual soma da linha ou coluna que você escolheu? ")).isdigit() or \
                (sum_player2 := int(sum_player2)) < 0:
            print("Digite uma entrada válida\n")

        sum_value_p1 = mod.sums(linecolumn, lc_number, matrix_p1)
        sum_value_p2 = mod.sums(linecolumn_p2, lc_number_p2, matrix_j2)
        bigger_row = max(copied_array_p1[lc_number])
        lower_row = mod.lower_line(copied_array_p1, lc_number)
        bigger_row_p2 = max(copied_array_p2[lc_number_p2])
        lower_row_p2 = mod.lower_line(copied_array_p2, lc_number_p2)

        # Se a diferença do jogador 1 for MENOR.
        if mod.evaluate(sum_value_p1, sum_player1) < mod.evaluate(sum_value_p2, sum_player2):
            if sum_player1 > sum_value_p1:
                historicP1[sum_player1] = "Maior"
                # Se a escolha for linha.
                if linecolumn == 1:
                    # Verifica localização do maior valor,
                    biggestrow = copied_array_p1[lc_number].index(bigger_row)
                    # Se o elemento for diferente de zero.
                    if copied_array_p1[lc_number][biggestrow] != 0:
                        # Aumenta placar para o jogador 1.
                        score_p1 += 1
                        # Revela elemento para o jogador.
                        hidden_array_p1[lc_number][biggestrow] = bigger_row
                        # Troca o elemento por zero na matriz copiada.
                        copied_array_p1[lc_number][biggestrow] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                # Se a escolha for COLUNA.
                elif linecolumn == 2:
                    biggestcolumn = mod.biggest_column(copied_array_p1, lc_number)
                    localization = mod.local(copied_array_p1, lc_number, biggestcolumn)
                    if copied_array_p1[localization][lc_number] != 0:
                        score_p1 += 1
                        hidden_array_p1[localization][lc_number] = biggestcolumn
                        copied_array_p1[localization][lc_number] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

            elif sum_player1 < sum_value_p1:
                historicP1[sum_player1] = "Menor"
                if linecolumn == 1:
                    lowerline = copied_array_p1[lc_number].index(lower_row)
                    if copied_array_p1[lc_number][lowerline] != 0:
                        score_p1 += 1
                        hidden_array_p1[lc_number][lowerline] = lower_row
                        copied_array_p1[lc_number][lowerline] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn == 2:
                    lowercolumn = mod.smallest_column(copied_array_p1, lc_number)
                    localization = mod.local(copied_array_p1, lc_number, lowercolumn)
                    if copied_array_p1[localization][lc_number] != 0:
                        score_p1 += 1
                        hidden_array_p1[localization][lc_number] = lowercolumn
                        copied_array_p1[localization][lc_number] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

            elif sum_player1 == sum_value_p1:
                historicP1[sum_player1] = "Igual"
                if linecolumn == 1:
                    sum_lin = 0
                    for coluna in range(len(matrix_p1)):
                        sum_lin += copied_array_p1[lc_number][coluna]
                    if sum_lin != 0:
                        lista = []
                        for lin in copied_array_p1[lc_number]:
                            if lin != 0:
                                lista.append(lin)
                        score_p1 += len(lista)
                        number_list = [matrix_p1[lc_number]]
                        hidden_array_p1[lc_number] = number_list[0]
                        for line in matrix_p1[lc_number]:
                            lugar = matrix_p1[lc_number].index(line)
                            copied_array_p1[lc_number][lugar] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn == 2:
                    column_list = mod.lista_coluna(matrix_p1, lc_number)
                    lista0 = mod.zeroed_matrix(len(matrix_p1))
                    soma = 0
                    for line in range(len(matrix_p1)):
                        hidden_array_p1[line][lc_number] = column_list[line]
                    for lin in range(len(matrix_p1)):
                        soma += copied_array_p1[lin][lc_number]
                    if soma != 0:
                        list_c = []
                        column_elements = mod.retornar_lista_col(copied_array_p1, lc_number)
                        for c in column_elements:
                            if c != 0:
                                list_c.append(c)
                        score_p1 += len(list_c)
                        for line in range(len(matrix_p1)):
                            copied_array_p1[line][lc_number] = lista0[line]
                    else:
                        print("\nCOLUNA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

        # caso a diferença da soma do jogador 2 seja menor
        elif mod.evaluate(sum_value_p1, sum_player1) > mod.evaluate(sum_value_p2, sum_player2):
            if sum_player2 > sum_value_p2:
                historicP2[sum_player2] = "Maior"
                if linecolumn_p2 == 1:
                    biggestrow = copied_array_p2[lc_number_p2].index(bigger_row_p2)
                    if copied_array_p2[lc_number_p2][biggestrow] != 0:
                        score_p2 += 1
                        hidden_array_p2[lc_number_p2][biggestrow] = bigger_row_p2
                        copied_array_p2[lc_number_p2][biggestrow] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn_p2 == 2:
                    biggestcolumn = mod.biggest_column(copied_array_p2, lc_number_p2)
                    localization = mod.local(copied_array_p2, lc_number_p2, biggestcolumn)
                    if copied_array_p2[localization][lc_number_p2] != 0:
                        score_p2 += 1
                        hidden_array_p2[localization][lc_number_p2] = biggestcolumn
                        copied_array_p2[localization][lc_number_p2] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

            elif sum_player2 < sum_value_p2:
                historicP2[sum_player2] = "Menor"
                if linecolumn_p2 == 1:
                    lowerline_p2 = copied_array_p2[lc_number_p2].index(lower_row_p2)
                    if copied_array_p2[lc_number_p2][lowerline_p2] != 0:
                        score_p2 += 1
                        hidden_array_p2[lc_number_p2][lowerline_p2] = lower_row_p2
                        copied_array_p2[lc_number_p2][lowerline_p2] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn_p2 == 2:
                    lower_column_p2 = mod.smallest_column(copied_array_p2, lc_number_p2)
                    localization = mod.local(copied_array_p2, lc_number_p2, lower_column_p2)
                    if copied_array_p2[localization][lc_number_p2] != 0:
                        score_p2 += 1
                        hidden_array_p2[localization][lc_number_p2] = lower_column_p2
                        copied_array_p2[localization][lc_number_p2] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

            elif sum_player2 == sum_value_p2:
                historicP2[sum_player2] = "Igual"
                if linecolumn_p2 == 1:
                    soma_lin_j2 = 0
                    for coluna in range(len(matrix_j2)):
                        soma_lin_j2 += copied_array_p2[lc_number_p2][coluna]
                    if soma_lin_j2 != 0:
                        listaj2 = []
                        for lin in copied_array_p2[lc_number_p2]:
                            if lin != 0:
                                listaj2.append(lin)
                        score_p2 += len(listaj2)
                        number_list = [matrix_j2[lc_number_p2]]
                        hidden_array_p2[lc_number_p2] = number_list[0]
                        for line in matrix_j2[lc_number_p2]:
                            lugar = matrix_j2[lc_number_p2].index(line)
                            copied_array_p2[lc_number_p2][lugar] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn_p2 == 2:
                    lista_coluna_j2 = mod.lista_coluna(matrix_j2, lc_number_p2)
                    lista0 = mod.zeroed_matrix(len(matrix_j2))
                    sum_player2 = 0
                    for line in range(len(matrix_j2)):
                        hidden_array_p2[line][lc_number_p2] = lista_coluna_j2[line]
                    for lin in range(len(matrix_j2)):
                        sum_player2 += copied_array_p2[lin][lc_number_p2]
                    if sum_player2 != 0:
                        lista_c_j2 = []
                        column_elements = mod.retornar_lista_col(copied_array_p2, lc_number_p2)
                        for c in column_elements:
                            if c != 0:
                                lista_c_j2.append(c)
                        score_p2 += len(lista_c_j2)
                        for line in range(len(matrix_j2)):
                            copied_array_p2[line][lc_number_p2] = lista0[line]
                    else:
                        print("\nCOLUNA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

        # Caso a diferença seja igual.
        if mod.evaluate(sum_value_p1, sum_player1) == mod.evaluate(sum_value_p2, sum_player2):
            if sum_player1 > sum_value_p1:
                historicP1[sum_player1] = "Maior"
                if linecolumn == 1:
                    biggestrow = copied_array_p1[lc_number].index(bigger_row)
                    if copied_array_p1[lc_number][biggestrow] != 0:
                        score_p1 += 1
                        hidden_array_p1[lc_number][biggestrow] = bigger_row
                        copied_array_p1[lc_number][biggestrow] = 0
                    else:
                        print("\nLINHA COMPLETA\n")

                elif linecolumn == 2:
                    biggest_column = mod.biggest_column(copied_array_p1, lc_number)
                    localization = mod.local(copied_array_p1, lc_number, biggest_column)
                    if copied_array_p1[localization][lc_number] != 0:
                        score_p1 += 1
                        hidden_array_p1[localization][lc_number] = biggest_column
                        copied_array_p1[localization][lc_number] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")

            elif sum_player1 < sum_value_p1:
                historicP1[sum_player1] = "Menor"
                if linecolumn == 1:
                    lowerline = copied_array_p1[lc_number].index(lower_row)
                    if copied_array_p1[lc_number][lowerline] != 0:
                        score_p1 += 1
                        hidden_array_p1[lc_number][lowerline] = lower_row
                        copied_array_p1[lc_number][lowerline] = 0
                    else:
                        print("\nLINHA COMPLETA\n")

                elif linecolumn == 2:
                    lowercolumn = mod.smallest_column(copied_array_p1, lc_number)
                    localization = mod.local(copied_array_p1, lc_number, lowercolumn)
                    if copied_array_p1[localization][lc_number] != 0:
                        score_p1 += 1
                        hidden_array_p1[localization][lc_number] = lowercolumn
                        copied_array_p1[localization][lc_number] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")

            elif sum_player1 == sum_value_p1:
                historicP1[sum_player1] = "Igual"
                if linecolumn == 1:
                    sum_row = 0
                    for coluna in range(len(matrix_p1)):
                        sum_row += copied_array_p1[lc_number][coluna]
                    if sum_row != 0:
                        numbers = []
                        for lin in copied_array_p1[lc_number]:
                            if lin != 0:
                                numbers.append(lin)
                        score_p1 += len(numbers)
                        number_list = [matrix_p1[lc_number]]
                        hidden_array_p1[lc_number] = number_list[0]
                        for line in matrix_p1[lc_number]:
                            lugar = matrix_p1[lc_number].index(line)
                            copied_array_p1[lc_number][lugar] = 0
                    else:
                        print("\nLINHA COMPLETA\n")

                elif linecolumn == 2:
                    lista_coluna = mod.lista_coluna(matrix_p1, lc_number)
                    lista0 = mod.zeroed_matrix(len(matrix_p1))
                    soma = 0
                    for line in range(len(matrix_p1)):
                        hidden_array_p1[line][lc_number] = lista_coluna[line]
                    for lin in range(len(matrix_p1)):
                        soma += copied_array_p1[lin][lc_number]
                    if soma != 0:
                        list_column = []
                        column_elements = mod.retornar_lista_col(copied_array_p1, lc_number)
                        for c in column_elements:
                            if c != 0:
                                list_column.append(c)
                        score_p1 += len(list_column)
                        for line in range(len(matrix_p1)):
                            copied_array_p1[line][lc_number] = lista0[line]
                    else:
                        print("\nCOLUNA COMPLETA\n")

            if sum_player2 > sum_value_p2:
                historicP2[sum_player2] = "Maior"
                if linecolumn_p2 == 1:
                    bigger_row_p02 = max(copied_array_p2[lc_number_p2])
                    biggestrow2 = copied_array_p2[lc_number_p2].index(bigger_row_p02)
                    if copied_array_p2[lc_number_p2][biggestrow2] != 0:
                        score_p2 += 1
                        hidden_array_p2[lc_number_p2][biggestrow2] = bigger_row_p02
                        copied_array_p2[lc_number_p2][biggestrow2] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn_p2 == 2:
                    biggest_column = mod.biggest_column(copied_array_p2, lc_number_p2)
                    localization = mod.local(copied_array_p2, lc_number_p2, biggest_column)
                    if copied_array_p2[localization][lc_number_p2] != 0:
                        score_p2 += 1
                        hidden_array_p2[localization][lc_number_p2] = biggest_column
                        copied_array_p2[localization][lc_number_p2] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

            elif sum_player2 < sum_value_p2:
                historicP2[sum_player2] = "Menor"
                if linecolumn_p2 == 1:
                    lower_row_p02 = mod.lower_line(copied_array_p2, lc_number_p2)
                    menor_linha_j2 = copied_array_p2[lc_number_p2].index(lower_row_p02)
                    if copied_array_p2[lc_number_p2][menor_linha_j2] != 0:
                        score_p2 += 1
                        hidden_array_p2[lc_number_p2][menor_linha_j2] = lower_row_p02
                        copied_array_p2[lc_number_p2][menor_linha_j2] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn_p2 == 2:
                    menor_coluna_j2 = mod.smallest_column(copied_array_p2, lc_number_p2)
                    localization = mod.local(copied_array_p2, lc_number_p2, menor_coluna_j2)
                    if copied_array_p2[localization][lc_number_p2] != 0:
                        score_p2 += 1
                        hidden_array_p2[localization][lc_number_p2] = menor_coluna_j2
                        copied_array_p2[localization][lc_number_p2] = 0
                    else:
                        print("\n COLUNA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

            elif sum_player2 == sum_value_p2:
                historicP2[sum_player2] = "Igual"
                if linecolumn_p2 == 1:
                    soma_lin_j2 = 0
                    for coluna in range(len(matrix_j2)):
                        soma_lin_j2 += copied_array_p2[lc_number_p2][coluna]
                    if soma_lin_j2 != 0:
                        listaj2 = []
                        for lin in copied_array_p2[lc_number_p2]:
                            if lin != 0:
                                listaj2.append(lin)
                        score_p2 += len(listaj2)
                        number_list = [matrix_j2[lc_number_p2]]
                        hidden_array_p2[lc_number_p2] = number_list[0]
                        for line in matrix_j2[lc_number_p2]:
                            lugar = matrix_j2[lc_number_p2].index(line)
                            copied_array_p2[lc_number_p2][lugar] = 0
                    else:
                        print("\nLINHA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

                elif linecolumn_p2 == 2:
                    lista_coluna_j2 = mod.lista_coluna(matrix_j2, lc_number_p2)
                    lista0 = mod.zeroed_matrix(len(matrix_j2))
                    sum_player2 = 0
                    for line in range(len(matrix_j2)):
                        hidden_array_p2[line][lc_number_p2] = lista_coluna_j2[line]
                    for lin in range(len(matrix_j2)):
                        sum_player2 += copied_array_p2[lin][lc_number_p2]
                    if sum_player2 != 0:
                        lista_c_j2 = []
                        column_elements = mod.retornar_lista_col(copied_array_p2, lc_number_p2)
                        for c in column_elements:
                            if c != 0:
                                lista_c_j2.append(c)
                        score_p2 += len(lista_c_j2)
                        for line in range(len(matrix_j2)):
                            copied_array_p2[line][lc_number_p2] = lista0[line]
                    else:
                        print("\nCOLUNA COMPLETA\n")
                    mod.show(hidden_array_p1, len(matrix_p1))
                    print()
                    mod.show(hidden_array_p2, len(matrix_j2))
                    mod.players_score(players, score_p1, score_p2)
                    mod.historic(players, historicP1, historicP2)

        # Se o valor que a função recebeu para "rounds" foi negativa, significa que os jogadores escolheram
        # finalizar a partida com tabuleiro completo.
        if rounds == -2:
            # Verifica se a matriz oculta do jogador 1 já foi completa.
            if matrix_p1 == hidden_array_p1:
                rounds = -1
            # Verifica se a matriz oculta do jogador 2 já foi completa.
            elif matrix_j2 == hidden_array_p2:
                rounds = -1
        # Se o valor que a função recebeu for positiva, significa que a partida irá acabar pelo número de rodadas.
        elif rounds >= 0:
            rounds += 1

            # Caso o tabuleiro fique completo antes de terminar a quantidade rodadas!
            if matrix_p1 == hidden_array_p1:
                rounds = -1
                amount = -1
            elif matrix_j2 == hidden_array_p2:
                rounds = -1
                amount = -1
    # Mostra quem ganhou a partida.
    mod.winner(score_p1, score_p2, players)
    print()
    # Mostra matriz revelada do jogador 1
    mod.show_sums(matrix_p1, len(matrix_p1), all_sums_line, all_sums_column)
    print()
    # Mostra matriz revelada do jogador 2.
    mod.show_sums(matrix_j2, len(matrix_j2), all_sums_line_p2, all_sums_column_p2)
