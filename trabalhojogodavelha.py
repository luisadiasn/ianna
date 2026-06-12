def criar_tabela():
    tabela = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(" ")
        tabela.append(linha)
    return tabela

def organizar_resposta(resp: str):
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

def desenhar_tabela(tabela: list):
    print(tabela)

def receber_resposta(resp: list, tabela: list, jogador_atual: int):
    k = resp[0]
    f = resp[1]
    contador_i = 0
    contador_j = 0
    tabela_final = []
    for i in tabela:
        contador_j = 0
        linha_final = []
        for j in i:
            if contador_i == k and contador_j == f:
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
    #metodo rudimentar de checar as diagonais
    if (lista[0][0] == jogador) and (lista[1][1] == jogador) and (lista [2][2] == jogador):
        return True
    if (lista[0][2] == jogador) and (lista[1][1] == jogador) and (lista [2][0] == jogador):
        return True
    return False
    



def checar_vitoria(tabela: list):
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
    


# se o jogador atual é 0, então é turno de x, se o jogador atual é 1 então é turno de O
pont_x = 0
pont_O = 0
jogador_atual = 0
resp_temp = input()
tabela = criar_tabela()
while True:
    resp = organizar_resposta(resp_temp)
    tabela = receber_resposta(resp, tabela, jogador_atual)

    if jogador_atual == 1:
        jogador_atual = 0
    else:
        jogador_atual = 1
    desenhar_tabela(tabela)
    if checar_vitoria(tabela) == "X":
        print("X ganhou!")
        pont_x += 1
        tabela = criar_tabela()
        desenhar_tabela(tabela)
    elif checar_vitoria(tabela) == "O":
        print("O ganhou!")
        pont_O += 1
        tabela = criar_tabela()
        desenhar_tabela(tabela)

    resp_temp = input()
