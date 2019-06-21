import ply.yacc as yacc
from minipascal_lexer import tokens
import minipascal_lexer
import sys

VERBOSE = 1

def p_program(p):
	'''program : PROGRAM ID SEMICOLON declaration_list
	| PROGRAM ID LPAREN argm_list RPAREN SEMICOLON declaration_list '''
	pass

def p_argm_list(p):
	'''argm_list : ID COMMA argm_list
	| ID'''
	pass

def p_declaration_list_1(p):
	'declaration_list : declaration_list  declaration' 
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	pass

def p_declaration(p):
	'''declaration : header_declaration 
    | fun_declaration
	| var_declaration'''
	pass

def p_header_declaration_1(p):
	'header_declaration : USES ID SEMICOLON'
	pass

def p_fun_declaration(p):
	'fun_declaration : FUNCTION ID LPAREN params RPAREN COLON identifiers SEMICOLON'
	pass

def p_var_declaration(p):
	'var_declaration : CONST '
	pass

def p_params_1(p):
    'params : params_list'
    pass

def p_params_list_1(p):
    'params_list : param SEMICOLON params_list'
    pass

def p_params_list_2(p):
    'params_list : param'
    pass

def p_param_1(p):
    'param : id_list COLON identifiers'
    pass

def p_id_list_1(p):
    'id_list : id_list COMMA ID'
    pass

def p_id_list_2(p):
    'id_list : ID'
    pass

def p_identifiers_1(p):
    'identifiers : INTEGER'
    pass

def p_identifiers_2(p):
    'identifiers : FLOAT'
    pass

def p_identifiers_3(p):
    'identifiers : BOOLEAN'
    pass

def p_identifiers_4(p):
    'identifiers : CHAR'
    pass

def p_empty(p):
	'empty :'
	pass


def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(minipascal_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion2.pas'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informa que Tu parser reconocio correctamente todo")
	#input()
