class Matrix:

    def __init__(self):
        self.pairingMatrix = []

    # (X,Y) in matrix
    def createMatrix(self, wordList):
        for X in range(0, len(wordList)):
            nlist = []
            self.pairingMatrix.append(nlist)
            for Y in range(0, len(wordList)):
                if wordList[X] == wordList[Y]:
                    self.pairingMatrix[X].append(1)
                else:
                    self.pairingMatrix[X].append(0)
