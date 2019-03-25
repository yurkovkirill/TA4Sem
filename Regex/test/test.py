import re

import sys

path = "txtfile"#short_file_middle0#txtfile

retcode = 0

statistics = {}
#<-respect&respect&respect^73#
with open(path) as f:
	for line in f:
		match= re.fullmatch('<-(!|[a-zA-Z])[a-zA-Z0-9]{,15}([&|^]((!|[a-zA-Z])[a-zA-Z0-9]{,15}))*#',line[:-1])
		if match:
			statistics.clear()
			print("string: '"+line[:-1]+"' is accepted!", end="\n")
			match1=re.findall('(!|[a-zA-Z])[a-zA-Z0-9]{,15}',line)
			for v in match1:
				if v not in statistics:
					statistics[v] = 1
				else:
					statistics[v] += 1
			print(statistics,end="\n\n")
		else:
			print("string: '"+line[:-1]+"' is not accepted!", end="\n\n")
f.close()
sys.exit(retcode)

