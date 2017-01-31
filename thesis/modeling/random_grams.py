### ------------------------------------------------------------
"""
creates random grammars and then generates models of them

the key of which files are linked to which grammars is stored
in the file "random_grams.txt"
"""
### ------------------------------------------------------------

import sys
sys.path.insert(0,"/home/ahilton/thesis-repo/")


import modeling
import grammar
import random


def main():

    ## File Constants ##
    blendfile = "random_grammars.blend"
    gramfile = "/home/ahilton/thesis-repo/modeling/random_grams.txt"

    ## Run Constants ##
    gramNum = 15
    runNum = 10

    labelList = ["A","B","C","D","E","F","G"]
    operList = ["grow","relabel","rest"]
    min_labels = 4
    max_labels = len(labelList)

    # Doing the run
    modeling.file_tools.save_as(blendfile)

    rulesList = []
    gramList = []
    textList = []
    for num in range(gramNum):
        labelNum = random.randint(min_labels,max_labels)
        labels = labelList[:labelNum]
        prods = []
        for letter in labels:
            oper = random.choice(operList)
            if oper == "grow":
                args = ""
                for i in range(3):
                    args += random.choice(labels)
            elif oper == "relabel":
                labelchoices = labels.copy()
                labelchoices.remove(letter)
                args = random.choice(labelchoices)
            elif oper == "rest":
                args = ""
            prods.append((oper,args))
        ruledic = dict(zip(labels,prods))
        rulesList.append(ruledic)
        textList.append("Gram{}:\n".format(num) + gram_toString(ruledic))
        
        curgram = grammar.runcontroller.setupRun(ruledic)
        gramList.append(curgram)
        
        modeling.file_tools.addScene("Gram{}".format(num))
        curgram.nRun(runNum)
        print("modeling Gram{}".format(num))
        modeling.gramConversion.modelGrammar(curgram)
        modeling.file_tools.save()

    textFile = open(gramfile,"w")
    for chunk in textList:
        textFile.write("{}\n".format("="*55)*2)
        textFile.write(chunk)
    textFile.close()

    
###
# takes in a string rule dictionary, and converts it to a readable string
###
def gram_toString(stringDic):
    retStr = ""
    for pair in sorted(stringDic.items()):
        retStr += "\t{} --> {}({})\n".format(pair[0],pair[1][0],pair[1][1])
    return retStr


if __name__ == "__main__":
    main()
