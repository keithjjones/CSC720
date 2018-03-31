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
    'expression : expression PLUS term'
    p[0] = ("PLUS", p[1], p[3])


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ("MINUS", p[1], p[3])


def p_expression_term(p):
    'expression : term'
    p[0] = ("EXPRESSION", p[1])


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = ("TIMES", p[1], p[3])


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = ("DIVIDE", p[1], p[3])


def p_term_factor(p):
    'term : factor'
    p[0] = ("FACTOR", p[1])


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = ("NUMBER", p[1])


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = ("PAREN", p[2])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

# Test it out
data = '''
(3 + 4) * 2
'''

result = parser.parse(data)
print(result)
print(type(result))


def crawl_ast(node):
    print("Node: {0}".format(node))
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
        print("Mult: {0}".format(output))
    elif node[0] == "DIVIDE":
        for i in range(1, len(results)):
            output = results[i-1] / results[i]
        print("Div: {0}".format(output))
    elif node[0] == "PLUS":
        for i in range(1, len(results)):
            output = results[i-1] + results[i]
        print("Add: {0}".format(output))
    elif node[0] == "MINUS":
        for i in range(1, len(results)):
            output = results[i-1] - results[i]
        print("Sub: {0}".format(output))

    print("Output: {0}".format(output))
    return output

crawl_ast(result)


# print("Output: {0}".format(output_string))

# while True:
#    try:
#        s = input('calc > ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)