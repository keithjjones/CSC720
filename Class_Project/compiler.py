# Script for lexer under Python for CSC720 class project.

import ply.lex as lex
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer import tokens

import llvmlite.ir as ll
import llvmlite.binding as llvm

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

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
print("YACC/AST Results: {0}".format(result))

module = ll.Module()
func_ty = ll.FunctionType(ll.IntType(64), [])
func = ll.Function(module, func_ty, name='main')

bb_entry = func.append_basic_block('entry')
irbuilder = ll.IRBuilder(bb_entry)

# tmp = irbuilder.add(func.args[0], func.args[1])
# ret = irbuilder.ret(tmp)


def crawl_ast(node, irb):
    # print("Node: {0}".format(node))
    results = []
    # Crawl each branch...
    for i in range(1, len(node)):
        if type(node[i]) is tuple:
            result = crawl_ast(node[i], irb)
            output = result
            results.append(result)
        else:
            output = ll.Constant(ll.IntType(64), node[i])

    # Now do the math...
    if node[0] == "TIMES":
        for i in range(1, len(results)):
            output = irb.mul(results[i-1], results[i])
        # print("Mult: {0}".format(output))
    elif node[0] == "DIVIDE":
        for i in range(1, len(results)):
            output = irb.udiv(results[i-1], results[i])
        # print("Div: {0}".format(output))
    elif node[0] == "PLUS":
        for i in range(1, len(results)):
            output = irb.add(results[i-1], results[i])
        # print("Add: {0}".format(output))
    elif node[0] == "MINUS":
        for i in range(1, len(results)):
            output = irb.sub(results[i - 1], results[i])
        # print("Sub: {0}".format(output))

    # print("Output: {0}".format(output))
    return output


result = crawl_ast(result, irbuilder)
irbuilder.ret(result)

print()
print('=== Begin LLVM IR')
print(module)
print('=== End LLVM IR')

# target = llvm.Target.from_triple("x86_64-pc-linux-gnu")
target = llvm.Target.from_default_triple()
target_machine = target.create_target_machine()
backing_mod = llvm.parse_assembly("")
engine = llvm.create_mcjit_compiler(backing_mod, target_machine)

mod = llvm.parse_assembly(str(module))
mod.verify()
# Now add the module and make sure it is ready for execution
engine.add_module(mod)
engine.finalize_object()
# engine.run_static_constructors()

engine.finalize_object()
print('=== Begin Assembly')
print(target_machine.emit_assembly(mod))
print('=== End Assembly')
print("Target machine: {0}".format(llvm.get_default_triple()))
