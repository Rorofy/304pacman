from src import globals


def mapVerif(tmpArr, a, b, c):
    if a < 0 or b < 0 or a >= len(globals.arr[b]) or b >= len(globals.arr):
        return False
    if globals.arr[b][a] == -4:
        return True
    if globals.arr[b][a] != -2:
        return False
    globals.arr[b][a] = c + 1
    tmpArr.append((a, b, c + 1))


class mapHandling():

    def pathfinder(fPos, pPos, wallChar, spaceChar):
        prev = [fPos]
        accessPath = False
        while len(prev) > 0:
            tmpArr = []
            for pPos in prev:
                if mapVerif(
                    tmpArr,
                    pPos[0],
                    pPos[1] - 1,
                    pPos[2]) or mapVerif(
                    tmpArr,
                    pPos[0] + 1,
                    pPos[1],
                    pPos[2]) or mapVerif(
                    tmpArr,
                    pPos[0],
                    pPos[1] + 1,
                    pPos[2]) or mapVerif(
                    tmpArr,
                    pPos[0] - 1,
                    pPos[1],
                        pPos[2]):
                    accessPath = True
                    tmpArr = []
                    break
            prev = tmpArr
        if accessPath:
            for e in globals.arr:
                tmpArr = ""
                for char in e:
                    mapSS = {-1: wallChar, -2: spaceChar, -
                             3: 'F', -4: 'P'}.get(char, str(char % 10))
                    tmpArr = tmpArr + mapSS
                print(tmpArr)
        else:
            exit(84)
