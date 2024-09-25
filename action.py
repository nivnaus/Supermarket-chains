from persistence import *

import sys

def main(args : list):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible
            currentProd = repo.products.find(id=splittedline[0])[0]
            ProdVars = vars(currentProd)

            if(int(splittedline[1]) < 0):
              if(ProdVars.get('quantity') >= -int(splittedline[1])):
                repo.products.update({'quantity': ProdVars.get('quantity') + int(splittedline[1])}, {'id':int(splittedline[0])})
                repo.activities.insert(Activitie(int(splittedline[0]), int(splittedline[1]),int(splittedline[2]),splittedline[3]))
            elif(int(splittedline[1]) > 0):
                repo.products.update({'quantity': ProdVars.get('quantity') + int(splittedline[1])}, {'id':int(splittedline[0])})
                repo.activities.insert(Activitie(int(splittedline[0]), int(splittedline[1]),int(splittedline[2]),splittedline[3]))

if __name__ == '__main__':
    main(sys.argv)