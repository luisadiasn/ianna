from random import sample

print('		Campo Minado')
nome=input('Seu nome: ').lower()
while True:
    medida=int(input('Medida do campo: '))
    if medida>=2 and medida<=9:
        m=medida*medida
        n_bombas=int(input(f'N de bombas ({medida}-{m}): '))
        if n_bombas>=medida and n_bombas<=m:
            linha=[]
            for i in range (1,medida+1):
                linha.append(i)
            print('#',*linha)
            for j in range(1,medida+1):
                print(j,'■ '*medida)
        break
linha,coluna:input('L C: ').split()


