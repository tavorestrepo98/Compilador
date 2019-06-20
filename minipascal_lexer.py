import ply.lex as lex, re
import sys

# list of tokens
tokens = (
    # Reserverd words
    'WRITELN',
    'TEXT',
    'READLN',
    'DIV',
    'OR',
    'AND',
    'NOT',
    'IF',
    'THEN',
    'ELSE',
    'OF',
    'WHILE',
    'DO',
    'USES',
    'BEGIN',
    'END',
    'READ',
    'WRITE',
    'VAR',
    'ARRAY',
    'PROCEDURE',
    'PROGRAM',
    'FUNCTION',
    'CASE',
    'FOR',
    'ASSERT',


    #Identifiers
    'INTEGER',
    'FLOAT',
    'BOOLEAN',
    'CHAR',

    # Symbols
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MINUSMINUS',
    'TIMES',
    'DIVIDE',
    'EQUAL',
    'DEQUAL',
    'LESS',
    'GREATER',
    'LESSEQUAL',
    'GREATEREQUAL',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'ISEQUAL',
    'DOT',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'POWER',
    'QUOTE',
    'COMILLA',

    # Others
    'ID',
    'NUMBER',

    # Commentaries
    'COMMENT',
    'COMMENT_LINE',
    'LBLOCK',
    'RBLOCK',
)

# Regular expressions rules for a simple tokens
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_DOT = r'.'
t_POWER = r'\^'
t_COMILLA = r'\''

def t_WRITELN(t):
    r'writeln'
    return t

# def t_TEXT(t):
#     r'\'(.|\n)*?\''
#     return t

def t_DIV(t):
    r'div'
    return t

def t_USES(t):
    r'uses'
    return t

def t_READLN(t):
    r'readln'
    return t

def t_OR(t):
    r'or'
    return t

def t_AND(t):
    r'and'
    return t

def t_NOT(t):
    r'not'
    return t

def t_IF(t):
    r'if'
    return t

def t_THEN(t):
    r'then'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ASSERT(t):
    r'assert'
    return t

def t_OF(t):
    r'of'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

def t_BEGIN(t):
    r'begin'
    return t

def t_END(t):
    r'end'
    return t

def t_READ(t):
    r'read'
    return t

def t_WRITE(t):
    r'write'
    return t

def t_VAR(t):
    r'var'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_PROCEDURE(t):
    r'procedure'
    return t

def t_PROGRAM(t):
    r'program'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_CASE(t):
    r'case'
    return t

def t_FOR(t):
    r'for'
    return t

def t_INTEGER(t):
    r'integer'
    return t

def t_FLOAT(t):
    r'real'
    return t

def t_BOOLEAN(t):
    r'Boolean'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'<>'
	return t

def t_ISEQUAL(t):
	r':='
	return t

def t_MINUSMINUS(t):
	r'Dec'
	return t

def t_PLUSPLUS(t):
	r'Inc'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_COMMENT(t):
    r'{(.|\n|{|})*}|\(\*(.|\n)*\*\)'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENT_LINE(t):
    r'//(.)*'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)


lexer = lex.lex(reflags=re.IGNORECASE)

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion.pas'
	f = open(fin, 'r')
	data = f.read()
	print (data.lower())
	lexer.input(data)
	test(data, lexer)
	input()
