import re
import time
import sys
import functions

import re
import ply.lex as lex
import ply.yacc as yacc
mas={}

correct = '0'
#path = "big_file_long"+correct


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






for i in range(1,11):
	#functions.gen(i,correct)
	path = "big_file_long"+str(i)+correct
	with open(path) as f:
		start = time.clock()
		pos = 0
		finish = time.clock()
		for line in f:
			parser.parse(line)
			mas.clear()
		finish = time.clock()
		print(100*(5*i), '# Time: ', finish-start)
	f.close()







