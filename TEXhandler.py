import sys

class TEXhandler:

	texFile = 0
	
	def __init__(self):
		self.texFile = 0
		
	def openAndCreateTexFile(self , fileName):
		try:
			self.texFile = open(fileName, 'w') #'w' is to used to clear opened file
		except:
			print("File {} could not be created".format(fileName))
			self.texFile = 0
		return
		
	def openReadOnlyTexFile(self , fileName):
		try:
			self.texFile = open(fileName, 'r') #'r' is to used to open in only read
		except:
			print("File {} could not be created".format(fileName))
			self.texFile = 0
		return
			
	def writeTextToTexFile(self , textToWrite):
		try:
			self.texFile.write(textToWrite)
		except:
			print("Error writing text into {}".format(self.texFile.name))
		return
	
	def closeTexFile(self):
		try:
			self.texFile.close()
			print("{} has been closed".format(self.texFile.name))
		except:
			print("Error closing File {}".format(self.texFile.name))
		return
		
	def getName(self):
		return self.texFile.name