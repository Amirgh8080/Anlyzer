
class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, ast):
        for node_type, node_value, children in ast:
            if node_type == 'assign':
                identifier, value = children
                if identifier in self.symbol_table:
                    print(f"Error: {identifier} already defined")
                else:
                    self.symbol_table[identifier] = value
            elif node_type == 'identifier':
                if node_value not in self.symbol_table:
                    print(f"Error: {node_value} not defined")
            elif node_type == 'number':
                pass # do nothing for now
            elif node_type == 'add':
                left, right = children
                if left[0] != 'number' or right[0] != 'number':
                    print("Error: can only add numbers")
            else:
                print(f"Error: unknown node type {node_type}")



from lexer import lexer
import ply.yacc as yacc
from parser import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_statement_expr(p):
    'statement : expression NEWLINE'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = ('ID', p[1])

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# parser = yacc.yacc(debug=True, write_tables=False)

def main():
    input_string = input()
    lexer.input(input_string)
    ast = parser.parse(input_string, lexer=lexer)
    print(ast)

main()
