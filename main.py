class SemanticAnalyzer:
  def __init__(self):
    self.symbol_table = {}

  def analyze(self, node):
    if isinstance(node, ProgramNode):
      for statement in node.Statements:
        self.analyze(statement)
    elif isinstance(node, VarDeclarationNode):
      var_name = node.VarName
      if var_name in self.symbol_table:
        raise Exception(f"Variable '{var_name}' already declared")
      self.symbol_table[var_name] = node.VarType
    elif isinstance(node, AssignmentNode):
      var_name = node.VarName
      if var_name not in self.symbol_table:
        raise Exception(f"Undefined variable '{var_name}'")
      var_type = self.symbol_table[var_name]
      expr_type = self.analyze(node.Expr)
      if var_type != expr_type:
        raise Exception(f"Type mismatch: expected '{var_type}', but got '{expr_type}'")
      return var_type
    elif isinstance(node, IfNode):
      condition_type = self.analyze(node.Condition)
      if condition_type != "bool":
        raise Exception(f"Condition must be of type 'bool', but got '{condition_type}'")
      self.analyze(node.IfStatement)
      if node.ElseStatement is not None:
        self.analyze(node.ElseStatement)
    elif isinstance(node, WhileNode):
      condition_type = self.analyze(node.Condition)
      if condition_type != "bool":
        raise Exception(f"Condition must be of type 'bool', but got '{condition_type}'")
      self.analyze(node.Statement)
    elif isinstance(node, PrintNode):
      self.analyze(node.Expr)
    elif isinstance(node, (NumberNode, BooleanNode)):
      return type(node).__name__.lower()
    elif isinstance(node, VariableNode):
      var_name = node.Name
      if var_name not in self.symbol_table:
        raise Exception(f"Undefined variable '{var_name}'")
      return self.symbol_table[var_name]
    elif isinstance(node, BinaryOpNode):
      left_type = self.analyze(node.Left)
      right_type = self.analyze(node.Right)
      if left_type != right_type:
        raise Exception(f"Type mismatch: '{left_type}' and '{right_type}'")
      return left_type
    elif isinstance(node, UnaryOpNode):
      expr_type = self.analyze(node.Expr)
      if expr_type != "bool":
        raise Exception(f"Unary operator '{node.Op}' requires a boolean expression, but got '{expr_type}'")
      return expr_type
    else:
      raise Exception(f"Unknown node type: {type(node).__name__}")





from lexer import Lexer
from parser import Parser
import SemanticAnalyzer

text = "var x: int = 42; if x > 0 then print true else print false"
lexer = Lexer(text)
parser = Parser(lexer)
ast = parser.parse()

analyzer = SemanticAnalyzer()
analyzer.analyze(ast)
print("Semantic analysis passed successfully!")
