#программа для генерации большого файла из строк по шаблону

import sys
import random

cor_title = '<-'
wrong_titles = ('<', '-', '<#', '<<')
titles = ('<-','<', '-', '<#', '<<')
ops = ('&','|','^')
cor_vars = ('respect', '!re', '73', 'w0m3n')
wrong_vars = ('', 'a2345678911131517', '!!!!!!r', 'wasd2134657809-=1111')
end = '#'
k = 1

def gen_str(mult, correct = '1'):
	string = ''
	if correct == '1':
		string = cor_title+random.choice(cor_vars)+(random.choice(ops)+random.choice(cor_vars))*k*mult
		for i in range(0,4):
			string += (random.choice(ops)+random.choice(cor_vars))*k*mult
	else:
		if random.randrange(0,2):
			string = random.choice(wrong_titles)+random.choice(cor_vars)*k*mult+(random.choice(ops)+random.choice(cor_vars))*k*mult
			for i in range(0,4):
				string += (random.choice(ops)+random.choice(cor_vars))*k*mult
		else:
			string = random.choice(titles)+random.choice(cor_vars)
			m = random.randrange(0,2)
			for i in range(0, m):
				string += (random.choice(ops)+random.choice(cor_vars))*k*mult
			string += (random.choice(ops)+random.choice(wrong_vars))*k*mult
			for i in range(0,4-m):
				string += (random.choice(ops)+random.choice(cor_vars))*k*mult
	string+=end
	return string












def gen(mult, correct):
	path = "big_file_long"+str(mult)
	with open(path+correct,'w') as f:
		for i in range(0, 100*(5*mult)):
			if correct == '1':
				if not i:
					f.write(gen_str(100))
				else:
					f.write('\n'+gen_str(100))
			else:
				if not i:
					f.write(gen_str(100, random.choice('01')))
				else:
					f.write('\n'+gen_str(100, random.choice('01')))
	f.close()
	pass

