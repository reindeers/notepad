#maybe use something else instead of multiple files, add try - catch
import os

class Note:
	def __init__(self, data, name=None, text=None):
		self.data = data
		self.name = name
		self.text = text

		
	def saveNote(self):
		f = open(self.data +'.txt', 'w')
		f.write(self.name + ' ' + self.text )
		f.close()

	def deleteNote(self, data):
		os.remove(data + '.txt')

	def editNote(self, data, name=None, text=None): 
		self.data = data
		if name != None:
			self.name = name
		if text != None:	
			self.text = text
		self.saveNote()

	def readNote(self, data):
		f = open(data + '.txt') 
		tmp = f.read()
		f.close() 
		return  tmp

newNote = Note('20140729', 'test', 'ttttt' )
newNote.saveNote()
newNote.editNote('20140729', text='lolo')
print(newNote.readNote('20140729'))
