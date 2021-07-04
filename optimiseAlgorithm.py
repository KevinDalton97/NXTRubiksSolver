
# This function takes in an algorithm and removes all unnecessary moves from it.
def optimiseAlgorithm(firstalgorithm):
    count = 0
    while count < 15:
        for i in range(len(firstalgorithm)):
            if i + 3 <= len(firstalgorithm):
                if firstalgorithm[i] == firstalgorithm[i + 1]:
                    toAdd = firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, toAdd + '2')
                elif (firstalgorithm[i] == 'U' and firstalgorithm[i + 1] == 'U2') or (
                        firstalgorithm[i] == 'U2' and firstalgorithm[i + 1] == 'U'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U`')
                elif (firstalgorithm[i] == 'F' and firstalgorithm[i + 1] == 'F2') or (
                        firstalgorithm[i] == 'F2' and firstalgorithm[i + 1] == 'F'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'F`')
                elif (firstalgorithm[i] == 'R' and firstalgorithm[i + 1] == 'R2') or (
                        firstalgorithm[i] == 'R2' and firstalgorithm[i + 1] == 'R'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'R`')
                elif (firstalgorithm[i] == 'B' and firstalgorithm[i + 1] == 'B2') or (
                        firstalgorithm[i] == 'B2' and firstalgorithm[i + 1] == 'B'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'B`')
                elif (firstalgorithm[i] == 'L' and firstalgorithm[i + 1] == 'L2') or (
                        firstalgorithm[i] == 'L2' and firstalgorithm[i + 1] == 'L'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'L`')
                elif (firstalgorithm[i] == 'D' and firstalgorithm[i + 1] == 'D2') or (
                        firstalgorithm[i] == 'D2' and firstalgorithm[i + 1] == 'D'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'D`')
                elif (firstalgorithm[i] == 'Y' and firstalgorithm[i + 1] == 'Y2') or (
                        firstalgorithm[i] == 'Y2' and firstalgorithm[i + 1] == 'Y'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y`')
                elif (firstalgorithm[i] == 'U' and firstalgorithm[i + 1] == 'U`') or (
                        firstalgorithm[i] == 'U`' and firstalgorithm[i + 1] == 'U'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                elif (firstalgorithm[i] == 'R' and firstalgorithm[i + 1] == 'R`') or (
                        firstalgorithm[i] == 'R`' and firstalgorithm[i + 1] == 'R'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                elif (firstalgorithm[i] == 'B' and firstalgorithm[i + 1] == 'B`') or (
                        firstalgorithm[i] == 'B`' and firstalgorithm[i + 1] == 'B'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                elif (firstalgorithm[i] == 'L' and firstalgorithm[i + 1] == 'L`') or (
                        firstalgorithm[i] == 'L`' and firstalgorithm[i + 1] == 'L'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                elif (firstalgorithm[i] == 'F' and firstalgorithm[i + 1] == 'F`') or (
                        firstalgorithm[i] == 'F`' and firstalgorithm[i + 1] == 'F'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                elif (firstalgorithm[i] == 'D' and firstalgorithm[i + 1] == 'D`') or (
                        firstalgorithm[i] == 'D`' and firstalgorithm[i + 1] == 'D'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                elif (firstalgorithm[i] == 'Y' and firstalgorithm[i + 1] == 'Y`') or (
                        firstalgorithm[i] == 'Y`' and firstalgorithm[i + 1] == 'Y'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                elif (firstalgorithm[i] == 'U' and firstalgorithm[i + 1] == 'D' and firstalgorithm[i + 2] == 'U'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U2')
                    firstalgorithm.insert(i + 1, 'D')
                elif (firstalgorithm[i] == 'D' and firstalgorithm[i + 1] == 'U' and firstalgorithm[i + 2] == 'D'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'D2')
                    firstalgorithm.insert(i + 1, 'U')
                elif (firstalgorithm[i] == 'L' and firstalgorithm[i + 1] == 'R' and firstalgorithm[i + 2] == 'L'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'L2')
                    firstalgorithm.insert(i + 1, 'R')
                elif (firstalgorithm[i] == 'R' and firstalgorithm[i + 1] == 'L' and firstalgorithm[i + 2] == 'R'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'R2')
                    firstalgorithm.insert(i + 1, 'L')
                elif (firstalgorithm[i] == 'F' and firstalgorithm[i + 1] == 'B' and firstalgorithm[i + 2] == 'F'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'F2')
                    firstalgorithm.insert(i + 1, 'B')
                elif (firstalgorithm[i] == 'B' and firstalgorithm[i + 1] == 'F' and firstalgorithm[i + 2] == 'B'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'B2')
                    firstalgorithm.insert(i + 1, 'F')

                elif (firstalgorithm[i] == 'U' and firstalgorithm[i + 1] == 'D2' and firstalgorithm[i + 2] == 'U'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U2')
                    firstalgorithm.insert(i + 1, 'D2')
                elif (firstalgorithm[i] == 'D' and firstalgorithm[i + 1] == 'U2' and firstalgorithm[i + 2] == 'D'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'D2')
                    firstalgorithm.insert(i + 1, 'U2')
                elif (firstalgorithm[i] == 'L' and firstalgorithm[i + 1] == 'R2' and firstalgorithm[i + 2] == 'L'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'L2')
                    firstalgorithm.insert(i + 1, 'R2')
                elif (firstalgorithm[i] == 'R' and firstalgorithm[i + 1] == 'L2' and firstalgorithm[i + 2] == 'R'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'R2')
                    firstalgorithm.insert(i + 1, 'L2')
                elif (firstalgorithm[i] == 'F' and firstalgorithm[i + 1] == 'B2' and firstalgorithm[i + 2] == 'F'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'F2')
                    firstalgorithm.insert(i + 1, 'B2')
                elif (firstalgorithm[i] == 'B' and firstalgorithm[i + 1] == 'F2' and firstalgorithm[i + 2] == 'B'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'B2')
                    firstalgorithm.insert(i + 1, 'F2')

                elif (firstalgorithm[i] == 'U2' and firstalgorithm[i + 1] == 'D2' and firstalgorithm[i + 2] == 'U') or (
                        firstalgorithm[i] == 'U' and firstalgorithm[i + 1] == 'D2' and firstalgorithm[i + 2] == 'U2'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U`')
                    firstalgorithm.insert(i + 1, 'D2')
                elif (firstalgorithm[i] == 'D2' and firstalgorithm[i + 1] == 'U2' and firstalgorithm[i + 2] == 'D') or (
                        firstalgorithm[i] == 'D' and firstalgorithm[i + 1] == 'U2' and firstalgorithm[i + 2] == 'D2'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'D`')
                    firstalgorithm.insert(i + 1, 'U2')
                elif (firstalgorithm[i] == 'L2' and firstalgorithm[i + 1] == 'R2' and firstalgorithm[i + 2] == 'L') or (
                        firstalgorithm[i] == 'L' and firstalgorithm[i + 1] == 'R2' and firstalgorithm[i + 2] == 'L2'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'L`')
                    firstalgorithm.insert(i + 1, 'R2')
                elif (firstalgorithm[i] == 'R2' and firstalgorithm[i + 1] == 'L2' and firstalgorithm[i + 2] == 'R') or (
                        firstalgorithm[i] == 'R' and firstalgorithm[i + 1] == 'L2' and firstalgorithm[i + 2] == 'R2'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'R`')
                    firstalgorithm.insert(i + 1, 'L2')
                elif (firstalgorithm[i] == 'F2' and firstalgorithm[i + 1] == 'B2' and firstalgorithm[i + 2] == 'F') or (
                        firstalgorithm[i] == 'F' and firstalgorithm[i + 1] == 'B2' and firstalgorithm[i + 2] == 'F2'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'F`')
                    firstalgorithm.insert(i + 1, 'B2')
                elif (firstalgorithm[i] == 'B2' and firstalgorithm[i + 1] == 'F2' and firstalgorithm[i + 2] == 'B') or (
                        firstalgorithm[i] == 'B' and firstalgorithm[i + 1] == 'F2' and firstalgorithm[i + 2] == 'B2'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'B`')
                    firstalgorithm.insert(i + 1, 'F2')
                elif firstalgorithm[i] == firstalgorithm[i + 1] and firstalgorithm[i] == firstalgorithm[i + 2]:
                    toAdd = firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, toAdd)

                elif firstalgorithm[i] == 'U`' and firstalgorithm[i + 1] == 'Y`' and firstalgorithm[i + 2] == 'U':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y`')
                elif firstalgorithm[i] == 'Y`' and firstalgorithm[i + 1] == 'U`' and firstalgorithm[i + 2] == 'Y`':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U`')
                elif firstalgorithm[i] == 'U' and firstalgorithm[i + 1] == 'Y`' and firstalgorithm[i + 2] == 'U`':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y`')
                elif firstalgorithm[i] == 'U`' and firstalgorithm[i + 1] == 'Y2' and firstalgorithm[i + 2] == 'U':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y2')
                elif firstalgorithm[i] == 'Y`' and firstalgorithm[i + 1] == 'U' and firstalgorithm[i + 2] == 'Y':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U')
                elif firstalgorithm[i] == 'U' and firstalgorithm[i + 1] == 'Y' and firstalgorithm[i + 2] == 'U`':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y')
                elif firstalgorithm[i] == 'U`' and firstalgorithm[i + 1] == 'Y2' and firstalgorithm[i + 2] == 'U`':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U2')
                    firstalgorithm.insert(i, 'Y2')
                elif firstalgorithm[i] == 'U' and firstalgorithm[i + 1] == 'Y' and firstalgorithm[i + 2] == 'U':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U2')
                    firstalgorithm.insert(i, 'Y')
                elif firstalgorithm[i] == 'U' and firstalgorithm[i + 1] == 'Y2' and firstalgorithm[i + 2] == 'U':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U2')
                    firstalgorithm.insert(i, 'Y2')
                elif (firstalgorithm[i] == 'U2' and firstalgorithm[i + 1] == 'Y' and firstalgorithm[i + 2] == 'U') or (
                        firstalgorithm[i] == 'U' and firstalgorithm[i + 1] == 'Y' and firstalgorithm[i + 2] == 'U2'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U`')
                    firstalgorithm.insert(i, 'Y')
                elif firstalgorithm[i] == 'U2' and firstalgorithm[i + 1] == 'Y2' and firstalgorithm[i + 2] == 'U2':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y2')
                elif firstalgorithm[i] == 'Y' and firstalgorithm[i + 1] == 'U' and firstalgorithm[i + 2] == 'Y':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y2')
                    firstalgorithm.insert(i, 'U')
                elif firstalgorithm[i] == 'Y' and firstalgorithm[i + 1] == 'U`' and firstalgorithm[i + 2] == 'Y':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y2')
                    firstalgorithm.insert(i, 'U`')
                elif firstalgorithm[i] == 'Y' and firstalgorithm[i + 1] == 'U2' and firstalgorithm[i + 2] == 'Y':
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y2')
                    firstalgorithm.insert(i, 'U2')
                elif (firstalgorithm[i] == 'Y' and firstalgorithm[i + 1] == 'U' and firstalgorithm[i + 2] == 'Y2') or (
                        firstalgorithm[i] == 'Y2' and firstalgorithm[i + 1] == 'U' and firstalgorithm[i + 2] == 'Y'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y`')
                    firstalgorithm.insert(i, 'U')
                elif (firstalgorithm[i] == 'Y' and firstalgorithm[i + 1] == 'U2' and firstalgorithm[i + 2] == 'Y2') or (
                        firstalgorithm[i] == 'Y2' and firstalgorithm[i + 1] == 'U2' and firstalgorithm[i + 2] == 'Y'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y`')
                    firstalgorithm.insert(i, 'U2')
                elif (firstalgorithm[i] == 'Y2' and firstalgorithm[i + 1] == 'U2' and firstalgorithm[i + 2] == 'Y2'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U2')

                elif (firstalgorithm[i] == 'U`' and firstalgorithm[i + 1] == 'U2') or (
                        firstalgorithm[i] == 'U2' and firstalgorithm[i + 1] == 'U`'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'U')
                elif (firstalgorithm[i] == 'F`' and firstalgorithm[i + 1] == 'F2') or (
                        firstalgorithm[i] == 'F2' and firstalgorithm[i + 1] == 'F`'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'F')
                elif (firstalgorithm[i] == 'R`' and firstalgorithm[i + 1] == 'R2') or (
                        firstalgorithm[i] == 'R2' and firstalgorithm[i + 1] == 'R`'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'R')
                elif (firstalgorithm[i] == 'B`' and firstalgorithm[i + 1] == 'B2') or (
                        firstalgorithm[i] == 'B2' and firstalgorithm[i + 1] == 'B`'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'B')
                elif (firstalgorithm[i] == 'L`' and firstalgorithm[i + 1] == 'L2') or (
                        firstalgorithm[i] == 'L2' and firstalgorithm[i + 1] == 'L`'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'L')
                elif (firstalgorithm[i] == 'D`' and firstalgorithm[i + 1] == 'D2') or (
                        firstalgorithm[i] == 'D2' and firstalgorithm[i + 1] == 'D`'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'D')
                elif (firstalgorithm[i] == 'Y`' and firstalgorithm[i + 1] == 'Y2') or (
                        firstalgorithm[i] == 'Y2' and firstalgorithm[i + 1] == 'Y`'):
                    del firstalgorithm[i]
                    del firstalgorithm[i]
                    firstalgorithm.insert(i, 'Y')
        count += 1
    return firstalgorithm


