import Sen_sm

class Sen:

	def __init__(self):
		self._fsm = Sen_sm.Sen_sm(self)
		self._is_acceptable = False
		self._buf = ""
		self._idict = {}

	def addbuf(self, ch):
		try:
			self._buf += str(ch)
		except BufferError:
			print("")
		pass

	def getBL(self):
		return len(self._buf)

	def reset(self):
		self._buf = ""
		pass

	def resetAll(self):
		self._buf = ""
		self._idict = {}
		pass


	def godict(self):
		if self._buf not in self._idict:
			self._idict[self._buf] = 1
		else:
			self._idict[self._buf] += 1
		pass


	def Acceptable(self):
		self._is_acceptable = True

	def Unacceptable(self):
		self._is_acceptable = False

	def ParseString(self, string):
		self._fsm.enterStartState()
		for c in string:
			ok = "&^|"
			if c == '<':
				self._fsm.Less()
			elif c == '-':
				self._fsm.Hyphen()
			elif c == '!':
				self._fsm.Exc()	
			elif c in ok:
				self._fsm.Op()	
			elif c == '#':
				self._fsm.Hashtag()
			elif c.isalpha():
				self._fsm.Let(c)
			elif c.isdigit():
				self._fsm.Num(c)
			elif ord(c) == 10:
				self._fsm.EOS()
			else:
				self._fsm.Unknown()

		return self._is_acceptable		

	def Reset(self):
		self._fsm.Reset()

	def show(self):
		for l in self._idict:
			print  l + " the number of using: " + str(self._idict[l])
		#print('\n')
		pass
