import numpy as np
def quicksort(array1, array2, left, right):
    i = left
    j = right
    med = array1[(left + right) // 2]
    while i <= j:
        while array1[i] < med:
            i += 1
        while array1[j] > med:
            j -= 1
        if i <= j:
            if array1[i] > array1[j]:
                t = array1[i]
                array1[i] = array1[j]
                array1[j] = t
                t = array2[i]
                array2[i] = array2[j]
                array2[j] = t
            i += 1
            j -= 1
    if left < j:
        quicksort(array1, array2, left, j)
    if right > i:
        quicksort(array1, array2, i, right)

# Чтение входного файла
with open('input_4.in', 'r') as f:
    arr = f.read()

# Парсинг массива
arr = arr.split('\n')
dim = int(arr[0].split(' ')[0])
graf = list()
for i in range(dim):
    graf.append(list(map(int, arr[i+1].split(' '))))

# Алгоритм Краскала
V = np.zeros([dim]) # Массив вершин
G = list() # Массив дуг
C = list() # Массив весов

for i in range(dim):
    for j in range(i + 1, dim):
        if graf[i][j] != 0:
            G.append([i, j])
            C.append(graf[i][j])

quicksort(C, G, 0, len(C) - 1)

ostov = 1
i = 0
print(C)
print(G)
giu = list()
while i < len(C):
    if V[G[i][0]] == 0 and V[G[i][1]] == 0:
        V[G[i][0]] = ostov
        V[G[i][1]] = ostov
        ostov += 1
    elif V[G[i][0]] == V[G[i][1]]:
        C.pop(i)
        G.pop(i)
        continue
    elif V[G[i][0]] != 0 and V[G[i][1]] == 0:
        V[G[i][1]] = V[G[i][0]]
    elif V[G[i][0]] == 0 and V[G[i][1]] != 0:
        V[G[i][0]] = V[G[i][1]]
    elif V[G[i][0]] < V[G[i][1]]:
        b = V[G[i][1]]
        for j in range(len(V)):
            if V[j] == b:
                V[j] = V[G[i][0]]
    elif V[G[i][1]] < V[G[i][0]]:
        b = V[G[i][0]]
        for j in range(len(V)):
            if V[j] == b:
                V[j] = V[G[i][1]]
    giu.append(G[i])
    i += 1
    print(giu)

print(V)

with open('input_4.out', 'w') as f:
    f.write(str(sum(C)) + '\n')

    matrix = np.zeros([dim, dim])
    for i in range(len(G)):
        matrix[G[i][0]][G[i][1]] = 1
        matrix[G[i][1]][G[i][0]] = 1
        G[i][0] += 1
        G[i][1] += 1

    for i in range(dim):
        for j in range(dim):
            if j != dim - 1:
                f.write(str(int(matrix[i][j])) + ', ')
            else:
                f.write(str(int(matrix[i][j])) + '\n')
    for i in range(len(G)):
        f.write('(' + str(G[i][0]) + ', ' + str(G[i][1]) + ')' + ' ')



