class SVGPlotter:

    def __init__(self, matrix=None):
        self.plotFile = None
        self.plotMatrix = matrix.pairingMatrix
        self.size = 5

    def SVGPlot(self, name=None):
        graphSize = str(self.size * len(self.plotMatrix))
        nname = name.split(".")
        path = nname[0] + ".svg"
        with open(path, "w") as file:
            file.write("<svg width=\"" + graphSize + "\" height=\"" + graphSize + "\">\n")
            self.plot(file)
            file.write("</svg>")

    def plot(self, file=None):
        coordY = 0
        for i in range (0, len(self.plotMatrix)):
            coordY += 5
            coordX = 0
            for j in range(0, len(self.plotMatrix)):
                draw = "<rect x=\"" + str(coordX) + "\" y=\"" + str(coordY) + "\" width=\"" + str(self.size) + "\" height=\"" + str(self.size)
                if self.plotMatrix[i][j] == 0:
                    draw += "\" style=\"fill:rgb(255,255,255)\" />\n"
                else:
                    draw += "\" style=\"fill:rgb(0,0,0)\" />\n"
                file.write(draw)
                coordX += 5



