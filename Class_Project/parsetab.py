
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEDIVIDE LPAREN MINUS NUMBER PLUS RPAREN TIMESexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMBERfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'LPAREN':([0,4,6,7,9,10,],[4,4,4,4,4,4,]),'PLUS':([1,2,3,5,8,11,12,13,14,15,],[-7,6,-6,-3,6,-1,-2,-8,-5,-4,]),'NUMBER':([0,4,6,7,9,10,],[1,1,1,1,1,1,]),'RPAREN':([1,3,5,8,11,12,13,14,15,],[-7,-6,-3,13,-1,-2,-8,-5,-4,]),'DIVIDE':([1,3,5,11,12,13,14,15,],[-7,-6,9,9,9,-8,-5,-4,]),'$end':([1,2,3,5,11,12,13,14,15,],[-7,0,-6,-3,-1,-2,-8,-5,-4,]),'MINUS':([1,2,3,5,8,11,12,13,14,15,],[-7,7,-6,-3,7,-1,-2,-8,-5,-4,]),'TIMES':([1,3,5,11,12,13,14,15,],[-7,-6,10,10,10,-8,-5,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,4,],[2,8,]),'term':([0,4,6,7,],[5,5,11,12,]),'factor':([0,4,6,7,9,10,],[3,3,3,3,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','parser.py',27),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','parser.py',32),
  ('expression -> term','expression',1,'p_expression_term','parser.py',37),
  ('term -> term TIMES factor','term',3,'p_term_times','parser.py',42),
  ('term -> term DIVIDE factor','term',3,'p_term_div','parser.py',47),
  ('term -> factor','term',1,'p_term_factor','parser.py',52),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser.py',57),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parser.py',62),
]
