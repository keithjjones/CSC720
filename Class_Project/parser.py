# Script for lexer under Python for CSC720 class project.

import ply.lex as lex
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer import tokens


class Node:
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        if children:
            self.children = children
        else:
            self.children = [ ]
        self.leaf = leaf


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = Node("+", [p[1], p[3]], p[2])


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = Node("+", [p[1], p[3]], p[2])


def p_expression_term(p):
    'expression : term'
    p[0] = Node("EXPRESSION", [p[1]], "EXPRESSION")


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = Node("*", [p[1], p[3]], p[2])


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = Node("/", [p[1], p[3]], p[2])


def p_term_factor(p):
    'term : factor'
    p[0] = Node("FACTOR", [p[1]], "FACTOR")


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = Node("NUMBER", [p[1]], "NUMBER")


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = Node("PAREN", [p[2]], "PAREN")


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

# Test it out
data = '''
3 + 4 * 2
'''

result = parser.parse(data)
print(result)
print(type(result))


def crawl_ast(node):
    output_string = ""
    if type(node) is Node:
        print("Node: {0}".format(node.leaf))
        for child in node.children:
            output_string += crawl_ast(child)
    else:
        print("Value: {0}".format(node))
        output_string = " {0} ".format(str(node))
    return output_string


output_string = crawl_ast(result)
print("Output: {0}".format(output_string))

# while True:
#    try:
#        s = input('calc > ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)