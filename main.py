from lexer import Lexer


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

from lexer import tokens, Lexer

def main():
    while True:
        try:
            input_string = input('Enter a mathematical expression: ')
            Lexer.input(input_string)
            for token in Lexer:
                print(token)
        except EOFError:
            break

if __name__ == '__main__':
    main()



main()