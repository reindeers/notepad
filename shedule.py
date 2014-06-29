class Shedule:
	def __init__(self):
		self.shdl = {'mnd': None, 'tsd': None, 'wnsd': None, 'thrsd': None, 'frd': None, 'strd': None, 'snd': None}

	def add(self, ss):
		for element in ss:
			if ss[element] != None:
				self.shdl[element] = ss[element]

	def printShedule(self):
		return self.shdl

ss = {'mnd': 1}
newShdl = Shedule()
newShdl.add(ss)
print(newShdl.printShedule())