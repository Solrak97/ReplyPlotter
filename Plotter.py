import sys
from App import matrix, plotter


#Aux functions
def getFixed(line):
    validated = ""
    for char in line:
        if char.isalpha() or char == " " or char == "\n":
            validated += char
    return validated.lower()

def unifyList(list):
    unified = []
    for element in list:
        unified += element.split()
    return unified

def correctFormat(path):
    correct = []
    with open(path) as file:
        for line in file:
            correct.append(getFixed(line))
    return unifyList(correct)



#Main function
def main(argv=None):
    if(len(sys.argv) == 2):
        filePath = sys.argv[1:]
        correctedFile = correctFormat(filePath[0])
        matrix.createMatrix(correctedFile)
        plotter.SVGPlot(filePath[0])

    else:
        print("There is an error on the number of parameters")
        exit(2)




if __name__ ==  '__main__':
    main(argv = sys.argv)