
# input number is between 0 and 2,147,483,647
def main(input: int):
    if(input >= 0 and input <= 2147483647):
        return ("[Semantic Analysis] positive int", input)
    else:
        return ("[Semantic Analysis] out of length", "")



if (__name__ == "__main__"):
    print(main(22))