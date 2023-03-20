import os 
# from typing import NamedTuple
# from enum import Enum
dir_path = os.path.dirname(os.path.realpath(__file__))

out_path =  os.path.join( dir_path,'output')

from typing import NamedTuple

class Bytecode(NamedTuple):
    """
    The Bytecode class.
    """
    function: int = 0
    level: int = 0
    value: int = 0

def get_dataFromMCT():
    data_lines = []
    with open(os.path.join( dir_path,'input.mct'), 'r') as f:
        # print(f.read())
        # data = f.read()
        for line in f.readlines():
            # print("line")
            # print(line)
            _data = line.replace('\n', ' ').split(" ")
            # print(_data)
            # data_line = {}
            
            byteCode = Bytecode()

            try:
                byteCode = Bytecode(int(_data[0]), int(_data[1]), int(_data[2]))
                # data_line["function"] = int(_data[0])
                # data_line["level"] = int(_data[1])
                # data_line["value"] = int(_data[2])
            except:
                raise
            
            data_lines.append(byteCode)
                
    return data_lines

def gen_MC(values: list):
    with open(os.path.join( out_path,'out.mc'), 'w') as f:
        value: Bytecode
        for value in values:
            # print(value)
            f.write("{0:03b}".format(value.function))
            f.write("{0:02b}".format(value.level))
            f.write("{0:011b}".format(value.value))
            # f.write("\n")


def MC_2_MCT():
    with open(os.path.join( out_path,'out.mc'), 'r') as f:
        # print(f.read())
        # data = f.read()
        results= []
        # lineNUM = 0

        # read 16 character and 
        MAX_IN_LINE = 16
        line = ""
        for char in f.read():
            line += char

            if(len(line) >= MAX_IN_LINE):
                byteCode = Bytecode(int(line[0:3], 2), int(line[3:5], 2), int(line[5:16], 2))
                line = ""
                results.append(byteCode)
        
        # print(results)


        # print(results)
    return results
            
def gen_MCT(values: list):
    with open(os.path.join( out_path,'out.mct'), 'w') as f:
        value: Bytecode
        for value in values:
            # print(value)
            f.write("{0} ".format(value.function))
            f.write("{0} ".format(value.level))
            f.write("{0} ".format(value.value))
            f.write("\n")


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

    with open(os.path.join( out_path,'out.asm'), 'w') as f:
        value: Bytecode
        for value in inputs:
            # print(value)
            f.write("{0} ".format(functionDisassembler[value.function]))
            f.write("{0} ".format(value.level))
            f.write("{0} ".format(value.value))
            f.write("\n")


def validateMCT_PerLine(input: Bytecode, lineNUM, isHeaderLine: bool=True):
    #TODO: ERROR CHECK LEVEL OF OPERATION IS SUPPORT OR NOT IF SELECT FUNCTION 0, 1, 5, 6, 7
    #TODO: ERROR CHECK OPERATION IF SELECT FUNCTION 7
    
    err = False

    functionNumber = input.function
    levelNumber = input.level
    valueNumber = input.value

    header = f"Line {lineNUM}"
    if(isHeaderLine == False):
        header = f"Bytes { (lineNUM - 1)*2 } - {(lineNUM - 1)*2 + 1}"


    try:
        # validate data range
        if(functionNumber > 7 ):
            err = True
            print(f"{header}: Invalid function [{functionNumber}]")
        if(levelNumber > 3 ):
            err = True
            print(f"{header}: Invalid level [{levelNumber}]")
        if(valueNumber > 2047 ):
            err = True
            print(f"{header}: Invalid value [{valueNumber}]")

        # validateCondition
        if(str(functionNumber) in "0 1 5 6 7" ):
            if(levelNumber != 0):
                err = True
                print(f"{header}: The function does not support level [{levelNumber}]")
        if (str(functionNumber) in "7"):
            if(valueNumber > 11 ):
                err = True
                print(f"{header}: Invalid operation [{valueNumber}]")

        if(err == True):
            # print(f"Line {lineNUM}: {errMessage}")
            raise ValueError(f".mct FILE ERROR.")
    except Exception as error:
        #  raise ValueError(f"{error.message}")
        # print('Caught this error: ' + repr(error))
        raise

def main():
    # # TODO: PHASE 1, .mct -> .mc
    data_MCT = get_dataFromMCT()
    # # [{'function': '0', 'level': '0', 'value': '0'}, {'function': '7', 'level': '0', 'value': '1'}, {'function': '2', 'level': '1', 'value': '2047'}, {'function': '3', 'level': '2', 'value': '79'}, {'function': '5', 'level': '0', 'value': '123'}]
    gen_MC(data_MCT)

    # # TODO: PHASE 4, validate .mct header error as Line
    for index, item in enumerate(data_MCT):
        validateMCT_PerLine(item, index+1, True)

    # TODO: PHASE 5, validate .mct header error as byte
    for index, item in enumerate(data_MCT):
        validateMCT_PerLine(item, index+1, False)

    # TODO: PHASE 2, .mc -> .mct
    inputs = MC_2_MCT()
    gen_MCT(inputs)

    # TODO: PHASE 3, .mc -> .asm
    disassembler(inputs)

if(__name__ == "__main__"):
    main()