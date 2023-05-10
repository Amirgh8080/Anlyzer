)
from lexer import lexer
import ply.yacc as yacc
from parser import *

def main():
    input_string = input()
    lexer.input(input_string)
    ast = parser.parse(input_string, lexer=lexer)
    print(ast)

main()
