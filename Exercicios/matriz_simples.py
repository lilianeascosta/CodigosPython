matriz = [[0, 0, 0], [0, 0, 0]]

for l in range(0,2):
    for c in range(0,2):
        matriz[l][c] = int(input(f'Digite um valor: '))

for l in range(0,2):
    for c in range(0,2):
        print(matriz[l][c], end = ' ')
    print()