class Matrix:

    def __init__(self):
        self.loadedFile = None
        self.fileContent = []
        self.pairingMatrix = []

    def loadFile(self, file=None):
        self.loadedFile = file
        for line in self.loadedFile:
            splitted = line.split()
            for word in splitted:
                self.fileContent.append(word)

    # (X,Y) in matrix
    def createMatrix(self):
        for X in range(0, len(self.fileContent)):
            nlist = []
            self.pairingMatrix.append(nlist)
            for Y in range(0, len(self.fileContent)):
                if self.fileContent[X] == self.fileContent[Y]:
                    self.pairingMatrix[X].append(1)
                else:
                    self.pairingMatrix[X].append(0)
        for i in range(0, len(self.fileContent)):
            for j in range(0, len(self.fileContent)):
                print(self.pairingMatrix[i][j], end="")
            print("")
