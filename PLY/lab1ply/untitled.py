import re
import ply.lex as lex
import ply.yacc as yacc
path = 'txtfile'
mas={}

tokens = (
    'OP','HASHTAG','START','VAR' , 'NEWLINE'
)

t_START = r'<-'
t_VAR = r'(\!|[a-zA-Z])[a-zA-Z0-9]{,15}'
t_HASHTAG = r'\#'
t_OP = r'[&|^]'

def t_error(t):
    t.lexer.skip(1)

def t_NEWLINE(t):
    r'\n+'
    # generate newline token   
    return t

lexer = lex.lex()

def p_sful(p):
	'fexpression : START expression HASHTAG NEWLINE'
	#print('sful ')
	p[0]=p[2]

def p_expr(p):
	'''expression : expression OP VAR
				  | VAR''' 
	if len(p) == 4:
		buf = p[3]
	else:
		buf=p[1]
	p[0]=p[1]
	#print(buf,'\n')
	#print('expr ')
	if buf not in mas:
		mas[buf] = 1
	else:
		mas[buf] +=1
def p_error(p):
    #print('here ')
    pass


#tampreg = '<-((!|[a-zA-Z])[a-zA-Z0-9]*([&|^]?(!|[a-zA-Z])+[a-zA-Z0-9]*)*)+#'

parser = yacc.yacc()

with open(path) as f:
	for line in f:
		print('#LINE : ',line[:-1])
		#parser.parse(line);
		#if print(parser.parse(line))
		if parser.parse(line):
			print('\nThe string is acceptable!\n')
		else:
			print('\nThe string is not acceptable!\n')
			mas={}
		for l in mas:
			print(l, ": the number of using: ", mas[l])
		mas={}
		print('\n')


f.close()

