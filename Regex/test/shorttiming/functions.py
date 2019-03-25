#программа для генерации большого файла из строк по шаблону

import sys
import random

cor_title = '<-'
wrong_titles = ( '-', '<#', '<<')
titles = ('<-','-', '<#', '<<')
ops = ('&','|','^')
cor_vars = ('respect', '!re', '73', 'w0m3n')
wrong_vars = ('', 'a2345678911131517', '!!!!!!r', 'wasd2134657809-=1111')
end = '#'
k = 1

def gen_str(mult, correct = '1'):
	string = ''
	if correct == '1':
		string = cor_title+random.choice(cor_vars)+(random.choice(ops)+random.choice(cor_vars))*k*1
		for i in range(0,2):
			string += (random.choice(ops)+random.choice(cor_vars))*k*1
	else:
		if random.randrange(0,2):
			string = random.choice(wrong_titles)+random.choice(cor_vars)*k*1+(random.choice(ops)+random.choice(cor_vars))*k*1
			for i in range(0,2):
				string += (random.choice(ops)+random.choice(cor_vars))*k*1
		else:
			string = random.choice(titles)
			m = 1
			for i in range(0, m):
				string += (random.choice(ops)+random.choice(cor_vars))*k*1
			string += (random.choice(ops)+random.choice(wrong_vars))*k*1
			for i in range(0,2-m):
				string += (random.choice(ops)+random.choice(cor_vars))*k*1
	string+=end
	return string


def gen(mult, correct):
	path = "short_file_middle"+str(mult)
	with open(path+correct,'w') as f:
		for i in range(0, mult*5000):
			if correct == '1':
				if not i:
					f.write(gen_str(mult))
				else:
					f.write('\n'+gen_str(mult))
			else:
				if not i:
					f.write(gen_str(mult, random.choice('01')))
				else:
					f.write('\n'+gen_str(mult, random.choice('01')))
	f.close()
	pass

