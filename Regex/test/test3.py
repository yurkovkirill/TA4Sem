import re

import sys

path = "txtfile"
statistics = {}
retcode = 0
line = '<-w0m3n&w0m3n&w0m3n&w0m3n&w0m3n&w0m3n&respect&respect&respect&respect&respect|73|73|73|73|73^73^73^73^73^73|73|73|73|73|73#'#'<-respect&respect&respect^3#'
match= re.fullmatch('<-(!|[a-zA-Z])[a-zA-Z0-9]{,15}([&|^]((!|[a-zA-Z])[a-zA-Z0-9]{,15}))*#',line)
if match:
	statistics.clear()
	print("string: '"+line+"' is accepted!", end="\n")
	match1=re.findall('!|[a-zA-Z][a-zA-Z0-9]*',line)
	for v in match1:
		if v not in statistics:
			statistics[v] = 1
		else:
			statistics[v] += 1
	print(statistics,end="\n\n")
else:
	print("string: '"+line+"' is not accepted!", end="\n\n")

#match1=re.findall('!|[a-zA-Z][a-zA-Z0-9]*',line)
#print(match1)
#for v in match1:
#			if v not in statistics:
#				statistics[v] = 1
#			else:
#				statistics[v] += 1
#print(statistics,end="\n\n")
sys.exit(retcode)

