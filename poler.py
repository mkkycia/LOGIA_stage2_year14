def poler(droga):
    lista = [[0, 0]]
    for i in droga:
        if i == 'p':
            lista.append([lista[-1][0]+1, lista[-1][1]])
        elif i == 'l':
            lista.append([lista[-1][0]-1, lista[-1][1]])
        elif i == 'g':
            lista.append([lista[-1][0], lista[-1][1]+1])
        elif i == 'd':
            lista.append([lista[-1][0], lista[-1][1]-1])
    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    for i in range(len(lista)):
        if lista[i][0] < minx:
            minx = lista[i][0]
        if lista[i][1] < miny:
            miny = lista[i][1]
        if lista[i][0] > maxx:
            maxx = lista[i][0]
        if lista[i][1] > maxy:
            maxy = lista[i][1]
    print(minx, maxx, miny, maxy)
    return (abs(minx) + abs(maxx)) * (abs(miny) + abs(maxy))

print(poler('lllgpdddd'))
