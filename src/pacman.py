from src import globals
from src import mapHandler as mapHandling


def pacman(mapContent, wallChar, spaceChar):
    fPos = None
    pPos = None
    lPos = 0
    for row in mapContent:
        row = row.strip('\n').strip('\r').strip('\n')
        globals.arr.append([])
        for i in range(0, len(row)):
            if row[i] == 'F':
                fPos = (i, lPos, 0)
            elif row[i] == 'P':
                pPos = (i, lPos)
            mapS = {'1': -1, '0': -2, 'F': -3, 'P': -4}.get(row[i], -5)
            if (mapS == -5):
                raise ValueError("Value Exception")
            globals.arr[lPos].append(mapS)
        lPos = lPos + 1
    if ((fPos is None) or (pPos is None)):
        raise ValueError("Value Exception")
    mapHandling.mapHandling.pathfinder(fPos, pPos, wallChar, spaceChar)
