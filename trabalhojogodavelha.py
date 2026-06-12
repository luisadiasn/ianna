#grupo: Ana luisa e Felipe Menezes

# -------------------------------------------------------------------------------
#                              * FUNÇÕES *
#--------------------------------------------------------------------------------

def criar_tabela():
    #essa função cria um array bidimensional 3x3 vazio
    tabela = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(" ")
        tabela.append(linha)
    return tabela

def organizar_resposta(resp: str):
    #organiza a resposta para ser interpretada de forma organizada
    respfinal = []
    for i in resp:
        respfinal.append(i)
    respfinal.sort()
    respfinal[0] = int(respfinal[0]) - 1
    letra = respfinal[1]
    if letra.lower() == "a":
        respfinal[1] = 0
    if letra.lower() == "b":
        respfinal[1] = 1
    if letra.lower() == "c":
        respfinal[1] = 2
    return respfinal

def desenhar_tabela(tab: list):
    #desenha a tabela para o usuario
    print("    A   B   C")
    print(f"1   {tab[0][0]}  | {tab[0][1]}  | {tab[0][2]}")
    print("   ----+----+----")
    print(f"2   {tab[1][0]}  | {tab[1][1]}  | {tab[1][2]}")
    print("   ----+----+----")
    print(f"3   {tab[2][0]}  | {tab[2][1]}  | {tab[2][2]}")

def receber_resposta(resp: list, tabela: list, jogador_atual: int):
    #recebe a resposta e atualiza a tabela para ser desenhada e checar a vitoria
    k = resp[0]
    f = resp[1]
    contador_i = 0
    contador_j = 0
    tabela_final = []
    for i in tabela:
        contador_j = 0
        linha_final = []
        for j in i:
            if contador_i == k and contador_j == f and j == " ":
                if jogador_atual == 1:
                    linha_final.append("O")
                else:
                    linha_final.append("X")
            elif j == "X":
                linha_final.append("X")
            elif j == "O":
                linha_final.append("O")
            else:
                linha_final.append(" ")
            contador_j += 1
        contador_i += 1
        tabela_final.append(linha_final)
    return tabela_final

def checar_em_volta(lista: list,pos_x: int, pos_y: int, jogador: str):
    #x é y e y é x em um plano cartesiano
    #checa em todas as direções em volta da posição atual
    contador_x = 0
    contador_y = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (pos_x + i > 2 or pos_y + j > 2) or (pos_x + i < 0 or pos_y + j < 0):
                continue
            if lista[pos_x + i][pos_y + j] == jogador:
                contador_x += 1
            if contador_x >= 3:
                return True
        contador_x = 0
        if (pos_x + i > 2 or pos_y + j > 2) or (pos_x + i < 0 or pos_y + j < 0):
                continue
        if lista[pos_x + i][pos_y + j] == jogador:
            contador_y += 1
        if contador_y >= 3:
            return True
    #metodo rudimentar de checar as diagonais e verticais
    if (lista[0][0] == jogador) and (lista[1][1] == jogador) and (lista[2][2] == jogador):
        return True
    if (lista[0][2] == jogador) and (lista[1][1] == jogador) and (lista[2][0] == jogador):
        return True
    if (lista[0][0] == jogador) and (lista[1][0] == jogador) and (lista[2][0] == jogador):
        return True
    if (lista[0][1] == jogador) and (lista[1][1] == jogador) and (lista[2][1] == jogador):
        return True
    if (lista[0][2] == jogador) and (lista[1][2] == jogador) and (lista[2][2] == jogador):
        return True

    return False
    



def checar_vitoria(tabela: list):
    #checa quem ganhou e retorna em string a pessoa que ganha
    contador_i = 0
    contador_j = 0
    for i in tabela:
        for j in i:
            if checar_em_volta(tabela, contador_i, contador_j, "X"):
                return "X"
            elif checar_em_volta(tabela, contador_i, contador_j, "O"):
                return "O"
            contador_j += 1
        contador_i += 1
    return False
    
def mostrar_placar(pont_x: int, pont_o: int):
    #mostra o placar no final do jogo
    print("            Player X         |          Player O")
    print(f"               {pont_x}                            {pont_o}")


# -------------------------------------------------------------------------------
#                              * CÓDIGO PRINCIPAL *
#--------------------------------------------------------------------------------
# se o jogador atual é 0, então é turno de x, se o jogador atual é 1 então é turno de O
pont_x = 0
pont_O = 0
jogador_atual = 0
print("         Jogo da Velha")
print("Marca do P1 >> X")
print("Marca do P2 >> O")

tabela = criar_tabela()
desenhar_tabela(tabela)
resp_temp = input()
contador_de_mov = 0
while True:
    resp = organizar_resposta(resp_temp)
    tabela = receber_resposta(resp, tabela, jogador_atual)
    #altera o turno do jogador
    if jogador_atual == 1:
        jogador_atual = 0
    else:
        jogador_atual = 1
    desenhar_tabela(tabela)
    quem_ganha = checar_vitoria(tabela)
    #checa quem ganha a partir da função
    if quem_ganha == "X":
        print("X ganhou!")
        pont_x += 1
        mostrar_placar(pont_x, pont_O)
        x = input("Enter para continuar")
        # reseta a tabela para outro jogo
        tabela = criar_tabela()
        desenhar_tabela(tabela)
    elif quem_ganha == "O":
        print("O ganhou!")
        pont_O += 1
        mostrar_placar(pont_x, pont_O)
        x = input("Enter para continuar")
        # reseta a tabela para outro jogo
        tabela = criar_tabela()
        desenhar_tabela(tabela)
    elif contador_de_mov >= 8:
        print("empate")
        mostrar_placar(pont_x, pont_O)
        # reseta a tabela para outro jogo
        tabela = criar_tabela()
        desenhar_tabela(tabela)
        contador_de_mov = 0

    resp_temp = input()
    contador_de_mov += 1
