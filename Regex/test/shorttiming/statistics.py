import re
import time
import sys
import functions

correct = '0'



statistics = {}

for i in range(1,11):
	functions.gen(i,correct)
	path = "short_file_middle"+str(i)+correct
	with open(path) as f:
		start = time.clock()
		pos = 0
		finish = time.clock()
		for line in f:
			match= re.fullmatch('<-!|[a-zA-Z][a-zA-Z0-9]{,15}([&|^]?!|[a-zA-Z][a-zA-Z0-9]{,15})*#',line[:-1])
			if match:
				statistics.clear()
				match=re.findall('!|[a-zA-Z][a-zA-Z0-9]*',line[:-1])
				for v in match:
					if v not in statistics:
						statistics[v] = 1
					else:
						statistics[v] += 1
		finish = time.clock()
		print(5000*i, '# Time: ', finish-start)
	f.close()


