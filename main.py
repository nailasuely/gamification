# ARQUIVO PRINCIPAL

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

# Importação dos arquivos secundários.
import board
import mod
import copy

option = ""

# Etapa de chamada das funções feitas para inicializar o jogo.
while option != 3:
    mod.menu()
    try:
        option = int(input("Escolha uma opção:\n"
                           " [1] [2] [3]\n"))
    except ValueError:
        print("\nDIGITE UMA OPÇÃO VÁLIDA!!!\n")
    if option == 1:
        # Lista para armazenar nome dos jogadores
        players = []
        while not (player1 := str(input("\nDigite o nome do jogador nº 1: \n"))).isalpha():
            print("DIGITE UM NOME VÁLIDO!!")
        players.append(player1)
        while not (player2 := str(input("\nDigite o nome do jogador nº 2: \n"))).isalpha():
            print("DIGITE UM NOME VÁLIDO!!")
        players.append(player2)

        # Criação da variável dentro de um laço de repetiação,
        # para verificar se o valor digitado está correto

        while not (mode := input("\nQual modo de jogo?\n"
                                 "[1] Um tabuleiro\n"
                                 "[2] Dois tabuleiros\n"
                                 " ")).isdigit() or (mode := int(mode)) < 1 or mode > 2:
            print("Digite uma opção válida!!")

        while not (difficulty := input("\nQual nível de dificuldade do jogo?\n"
                                       "[1] FÁCIL\n"
                                       "[2] MÉDIO\n"
                                       "[3] DIFÍCIL\n"
                                       " ")).isdigit() or (difficulty := int(difficulty)) < 1 or difficulty > 3:
            print("Digite uma opção válida!!")

        while not (finish := input("\nComo a partida termina?\n"
                                   "[1] Número de rodadas\n"
                                   "[2] Tabuleiro completo\n"
                                   " ")).isdigit() or (finish := int(finish)) < 1 or finish > 2:
            print("Digite uma opção válida!!")

        # Verificar se o jogo vai parar pelo número de rodadas.
        if finish == 1:
            while not (amount := input("\nDigite a quantidade de rodadas: ")).isdigit() \
                    or (amount := int(amount)) % 2 == 0:
                print("Digite um número IMPAR!!")
            rounds = 0

        elif finish == 2:
            amount = -1
            rounds = -2
        # Verificação do modo e da dificuldade escolhida.
        if mode == 1 and difficulty == 1:
            # Matriz principal para o nível fácil.
            easy_matrix = mod.level(3, 30)
            # Matriz oculta.
            easy_hidden_matrix = mod.hidden_matrix(3)
            # Matriz copiada.
            copied_matrix_easy = copy.deepcopy(easy_matrix)
            # Chamada da função.
            game = board.board_one(
                easy_matrix, easy_hidden_matrix, copied_matrix_easy, players, amount, rounds)

        elif mode == 1 and difficulty == 2:
            # Matrizes no nível médio para um tabuleiro.
            med_matrix = mod.level(4, 60)
            copied_matrix_med = copy.deepcopy(med_matrix)
            hidden_med_matrix = mod.hidden_matrix(4)

            game = board.board_one(
                med_matrix, hidden_med_matrix, copied_matrix_med, players, amount, rounds)

        elif mode == 1 and difficulty == 3:
            # Matrizes para o nível difícil.
            hard_hidden_matrix = mod.hidden_matrix(5)
            hard_matrix = mod.level(5, 100)
            copied_matrix_hard = copy.deepcopy(hard_matrix)
            # Chamada da função.
            game = board.board_one(
                hard_matrix, hard_hidden_matrix, copied_matrix_hard, players, amount, rounds)

        elif mode == 2 and difficulty == 1:
            # Matrizes no nível facil para dois tabueleiros.
            easy_matrix_p1 = mod.level(3, 30)
            easy_matrix_p2 = mod.level(3, 30)
            # Matrizes copiadas para os dois jogadores.
            easy_matrix_copied_p1 = copy.deepcopy(easy_matrix_p1)
            easy_matrix_copied_p2 = copy.deepcopy(easy_matrix_p2)
            # Matrizes ocultas para os dois jogadores.
            easyhidden_matrix_p1 = mod.hidden_matrix(3)
            easyhidden_matrix_p2 = mod.hidden_matrix(3)
            # Chamada da função.
            game = board.two_boards(
                easy_matrix_p1, easy_matrix_p2,
                easyhidden_matrix_p1, easyhidden_matrix_p2,
                easy_matrix_copied_p1, easy_matrix_copied_p2,
                players, amount, rounds)

        elif mode == 2 and difficulty == 2:
            # Matrizes no nível médio para dois tabuleiros.
            med_matrix_p1 = mod.level(4, 60)
            matriz_med_p2 = mod.level(4, 60)
            # Matrizes copiadas para os dois jogadores.
            med_matrix_copied_p1 = copy.deepcopy(med_matrix_p1)
            med_matrix_copied_p2 = copy.deepcopy(matriz_med_p2)
            # Matrizes ocultas para os dois jogadores.
            medhidden_matrix_p1 = mod.hidden_matrix(4)
            medhidden_matrix_p2 = mod.hidden_matrix(4)
            # Chamada da função.
            game = board.two_boards(
                med_matrix_p1, matriz_med_p2,
                medhidden_matrix_p1, medhidden_matrix_p2,
                med_matrix_copied_p1, med_matrix_copied_p2,
                players, amount, rounds)

        elif mode == 2 and difficulty == 3:

            # Matrizes no nível díficil para dois tabuleiros.
            hard_matrix_p1 = mod.level(5, 100)
            hard_matrix_p2 = mod.level(5, 100)
            # Matrizes copiadas para os dois tabuleiros.
            hard_matrix_copied_p1 = copy.deepcopy(hard_matrix_p1)
            hard_matrix_copied_p2 = copy.deepcopy(hard_matrix_p2)
            # Matrizes ocultas para os dois jogadores.
            hardhidden_matrix_p1 = mod.hidden_matrix(5)
            hardhidden_matrix_p2 = mod.hidden_matrix(5)
            # Chamada da função.
            game = board.two_boards(
                hard_matrix_p1, hard_matrix_p2,
                hardhidden_matrix_p1, hardhidden_matrix_p2,
                hard_matrix_copied_p1, hard_matrix_copied_p2,
                players, amount, rounds)

    elif option == 2:
        # Opção para visualizar instruções do jogo.
        mod.instructions()
    # Caso o jogador não digite uma opção correta.
    elif option == 3:
        print("O jogo das Somas Esquecidas foi finalizado!")
    else:
        print("\nDIGITE UMA OPÇÃO VÁLIDA!!!\n")
