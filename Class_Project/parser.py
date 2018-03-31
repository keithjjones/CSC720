# Script for lexer under Python for CSC720 class project.

import ply.lex as lex
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer import tokens


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)


def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = ("PLUS", p[1], p[3])


def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = ("MINUS", p[1], p[3])


def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = ("TIMES", p[1], p[3])


def p_expression_divide(p):
    'expression : expression DIVIDE expression'
    p[0] = ("DIVIDE", p[1], p[3])


def p_expression_term(p):
    'expression : NUMBER'
    p[0] = ("NUMBER", p[1])


def p_expression_expr(p):
    'expression : LPAREN expression RPAREN'
    p[0] = ("PAREN", p[2])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

# Test it out
data = '''
3 + 4 * 2
'''

input_string = input("Give me some math or press enter for a simple example: ")
if input_string.strip() == "":
    input_string = data
print("Using Data: {0}".format(input_string))
result = parser.parse(input_string)
print("YACC Results: {0}".format(result))


def crawl_ast(node):
    # print("Node: {0}".format(node))
    results = []
    # Crawl each branch...
    for i in range(1, len(node)):
        if type(node[i]) is tuple:
            result = crawl_ast(node[i])
            output = result
            results.append(result)
        else:
            output = node[i]

    # Now do the math...
    if node[0] == "TIMES":
        for i in range(1, len(results)):
            output = results[i-1] * results[i]
        # print("Mult: {0}".format(output))
    elif node[0] == "DIVIDE":
        for i in range(1, len(results)):
            output = results[i-1] / results[i]
        # print("Div: {0}".format(output))
    elif node[0] == "PLUS":
        for i in range(1, len(results)):
            output = results[i-1] + results[i]
        # print("Add: {0}".format(output))
    elif node[0] == "MINUS":
        for i in range(1, len(results)):
            output = results[i-1] - results[i]
        # print("Sub: {0}".format(output))

    # print("Output: {0}".format(output))
    return output


result = crawl_ast(result)
print()
print("Calculated Result: {0}".format(result))
