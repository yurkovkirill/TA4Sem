#!/usr/bin/env python

import sys

import Sen

#path = 'short_file_middle0'#txtfile

retcode = 0

appobject = Sen.Sen()
import re
import time
import sys
import gen_file_long

correct = '0'


statistics = {}

for i in range(1,11):
	#gen_file_long.gen(i,correct)
	path = 'big_file_long'+str(i)+correct
	with open(path) as f:
		start = time.clock()
		pos = 0
		finish = time.clock()
		for line in f:
			if appobject.ParseString(str(line)) == False:
				result = "not acceptable"
				retcode = 1
			else:
				result = "acceptable"
				#appobject.show() 
			#print('The string: %s is %s.\n' % (line, result))
			appobject.Reset()
		finish = time.clock()
		print(100*(5*i), '# Time: ', finish-start)
	f.close()
sys.exit(retcode)
