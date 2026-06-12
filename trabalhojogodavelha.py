def criar_tabela():
    tabela = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append("V")
        tabela.append(linha)
    return tabela

def desenhar_tabela(pos: list, tabela: list):
    pass

def receber_resposta(resp: list, tabela: list):
    pass

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



x = "A4"
print(organizar_resposta(x))