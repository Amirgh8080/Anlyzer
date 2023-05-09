import ply.lex as lex

# class Lexer:
#     # List of token names
#     tokens = (
#         'ID',
#         'NUMBER',
#         'PLUS',
#         'MINUS',
#         'TIMES',
#         'DIVIDE',
#         'LPAREN',
#         'RPAREN',
#     )
#
#     # Regular expression rules for simple tokens
#     t_PLUS    = r'\+'
#     t_MINUS   = r'-'
#     t_TIMES   = r'\*'
#     t_DIVIDE  = r'/'
#     t_LPAREN  = r'\('
#     t_RPAREN  = r'\)'
#
#     # A regular expression rule with some action code
#     def t_NUMBER(self, t):
#         r'\d+'
#         t.value = int(t.value)
#         return t
#
#     # Define a rule so we can track line numbers
#     def t_newline(self, t):
#         r'\n+'
#         t.lexer.lineno += len(t.value)
#
#     # A string containing ignored characters (spaces and tabs)
#     t_ignore  = ' \t'
#
#     # Error handling rule
#     def t_error(self, t):
#         print("Illegal character '%s'" % t.value[0])
#         t.lexer.skip(1)
#
#     # Build the lexer
#     def build(self, **kwargs):
#         self.lexer = lex.lex(module=self, **kwargs)
#
#     # Test the lexer
#     def test(self, data):
#         self.lexer.input(data)
#         for tok in self.lexer:
#             print(tok)

import ply.lex as lex

tokens = [
    'ID',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'LPAREN',
    'RPAREN',
]


class Lexer:

    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_MULT = r'\*'
    t_DIV = r'\/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    t_ignore = ' \t\n'

    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        return t

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    lexer = lex.lex()
