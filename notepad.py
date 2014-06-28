class Note:
	def __init__(self, data, name=None, text=None):
		self.data = data
		self.name = name
		self.text = text
		
	def saveNote(self):
		f = open(self.data +'.txt', 'w')
		f.write(self.name + self.text )
		f.close()
	def deleteNewNote(self):
		pass
	def editNote(self): #reload data
		pass
	def readNote(self, data):
		f = open(data + '.txt') 
		return f.read() 
		

newNote = Note('20140729', 'test', 'ttttt' )
newNote.saveNote()
print(newNote.readNote('20140729'))