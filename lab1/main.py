import os 
from typing import NamedTuple
from enum import Enum
_path = os.path.dirname(os.path.realpath(__file__))

dir_path = os.path.join( _path,'output')
# print(dir_path)


def gen_txt(value):
    with open(os.path.join( dir_path,'output_txt.txt'), 'w') as f:
        f.write(str(value))


def gen_py(value):
    with open(os.path.join( dir_path,'code_py.py'), 'w') as f:
        f.write(f"print({value})")

def gen_c(value):
    with open(os.path.join( dir_path,'code_c.c'), 'w') as f:
        f.write(f"#include <stdio.h>"+ os.linesep)
        f.write(f"int main()"+ os.linesep)
        f.write(r"{"+ os.linesep)
        f.write(f"printf({value});"+ os.linesep)
        f.write(f"return 0;"+ os.linesep)
        f.write(r"}"+ os.linesep)


def gen_cpp(value):
    with open(os.path.join( dir_path,'code_cPlus.cpp'), 'w') as f:
        f.write(f"#include <iostream>"+ os.linesep)
        f.write(r"int main() {"+ os.linesep)
        f.write(f"std::cout << '{value}';"+ os.linesep)
        f.write(f"return 0;"+ os.linesep)
        f.write(r"}"+ os.linesep)

def gen_cs(value):
    with open(os.path.join( dir_path,'code_cSharp.cs'), 'w') as f:
        f.write("""
// C# program to print Hello World!
using System;
  
// namespace declaration
namespace HelloWorldApp {
      
    // Class declaration
    class HelloWorld {
          
        // Main Method
        static void Main(string[] args) {
              
            // statement
            // printing number
            """+ os.linesep)
        f.write(f"""
            Console.WriteLine({value});
            """+ os.linesep)
        f.write("""
                          
            // To prevents the screen from 
            // running and closing quickly
            Console.ReadKey();
        }
    }
}
            """+ os.linesep)

def main(value: int):
    print("main lab 1")
    # create source file 
    gen_txt(value)
    gen_py(value)
    gen_c(value)
    gen_cpp(value)
    gen_cs(value)





if (__name__ == "__main__"):
    main(22)