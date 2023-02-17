import os 
# from typing import NamedTuple
# from enum import Enum
dir_path = os.path.dirname(os.path.realpath(__file__))

out_path =  os.path.join( dir_path,'output')

def get_dataFromMCT():
    with open(os.path.join( dir_path,'input.mct'), 'r') as f:
        # print(f.read())
        data = f.read()
    return data

def gen_MC(values: list):
    with open(os.path.join( out_path,'out.mc'), 'w') as f:
        for value in values:
            f.write("{0:03b}".format(value[0]))
            f.write("{0:02b}".format(value[1]))
            f.write("{0:011b}".format(value[2])+ "\n")


def MC_2_MCT():
    with open(os.path.join( out_path,'out.mc'), 'r') as f:
        # print(f.read())
        # data = f.read()
        results= []
        lineNUM = 0
        for line in f.readlines():
            lineNUM+=1
            # print(line)

            validateMC(line, lineNUM)

            value = []
            value.append(int(line[0:3], 2))
            value.append(int(line[3:5], 2))
            value.append(int(line[5:16], 2))

            results.append(value)


        print(results)
    return results
            


def validateMC(input: list, lineNUM):
    #TODO: ERROR CHECK LEVEL OF OPERATION IS SUPPORT OR NOT IF SELECT FUNCTION 0, 1, 5, 6, 7
    #TODO: ERROR CHECK OPERATION IF SELECT FUNCTION 7
    errMessage=""
    functionNumber = int(input[0])
    levelNumber = int(input[1])
    valueNumber = int(input[0])

    try:
        # validate data range
        if(functionNumber > 3 ):
            errMessage = f"Invalid function [{input[0]}]"
            
        if(levelNumber > 2 ):
            errMessage = f"Invalid level [{input[1]}]"
        if(valueNumber > 11 ):
            errMessage = f"Invalid value [{input[2]}]"

        # validateCondition
        if(str(functionNumber) in "01567" ):
            if(levelNumber != 0):
                errMessage = f"The function does not support level [{levelNumber}]"
        elif (str(functionNumber) in "7"):
            if(valueNumber > 7 ):
                errMessage = f"Invalid operation [{input[2]}]"

        if(errMessage != ""):
            raise ValueError(f"Line {lineNUM}: {errMessage}")
    except:
         raise ValueError(f"Line {lineNUM}:  ERROR ")

def disassembler(inputs: list):
    functionDisassembler = {
        0: "LIT",
        1: "INT",
        2: "LOD",
        3: "STO",
        4: "CAL",
        5: "JMP",
        6: "JPC",
        7: "OPR",      
    }
    
    results = []
    for input in inputs:
        value = []
        value.append(functionDisassembler[input[0]])
        value.append(input[1])
        value.append(input[2])
        results.append(value)

    print(results)
    return results
    

def main():
    data = get_dataFromMCT()
    gen_MC([[1,2,200], [1,2,200], [1,2,2005] ])
    inputs = MC_2_MCT()
    disassembler(inputs)


    # convert to binary


if(__name__ == "__main__"):
    main()