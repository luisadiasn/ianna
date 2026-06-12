def criar_tabela():
    tabela = []
    for i in range(3):
        for j in range(3):
            tabela.append("V")

def desenhar_tabela(pos: list):
    pass

def receber_resposta(resp: list):
    pass

def organizar_resposta(resp: str):
    respfinal = []
    for i in resp:
        respfinal.append(i)
    respfinal.sort()
    return respfinal



x = "A4"
print(organizar_resposta(x))