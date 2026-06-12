def criar_tabela():
    tabela = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(" ")
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

def exibir_tabuleiro(tab):
        print("    A   B   C")
        print(f"1   {tab[0][0]}  | {tab[0][1]}  | {tab[0][2]}")
        print("   ---+---+---")
        print(f"2   {tab[1][0]}  | {tab[1][1]}  | {tab[1][2]}")
        print("   ---+---+---")
        print(f"3   {tab[2][0]}  | {tab[2][1]}  | {tab[2][2]}")
        
def placar():
    

caractere=input().upper()
if caractere=='X' or caractere=='O':
    tabuleiro=[
        ['','',''],
        ['','',''],
        ['','','']
        ]


x = "A4"
print(organizar_resposta(x))