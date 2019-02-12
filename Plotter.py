import sys
from App import matrix, plotter
def main(argv=None):
    if(len(sys.argv) == 2):
        filePath = sys.argv[1:]
        with open(filePath[0]) as file:
            matrix.loadFile(file)
            matrix.createMatrix()
        plotter.SVGPlot(filePath[0])



    else:
        print("There is an error on the number of parameters")
        exit(2)




if __name__ ==  '__main__':
    main(argv = sys.argv)