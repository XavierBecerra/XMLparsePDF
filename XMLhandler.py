import xml.etree.ElementTree as ET

class XMLhandler:

	xmlTree = 0
	xmlPosition = 0
	xmlText = ""
	xmlElementList = []
	
	def __init__(self):
		self.xmlTree = 0
		self.xmlPosition = 0
		self.xmlText = ""
		self.xmlElementList = []
	
	def setXMLfileToBeParsed( self, fileName ):
		self.assignElementTreeSuccessfully( fileName )
		return
	
	def assignElementTreeSuccessfully(self, fileName ):
		try:
			self.xmlTree = ET.parse(fileName)
			self.getRootFromElementTree()
		except FileNotFoundError:
			print("File {} Not Found".format(fileName))
			
		return
	
	def getRootFromElementTree(self):
		self.xmlPosition = self.xmlTree.getroot()
		return

	def getListOfTagsInXML(self):
		for elem in self.xmlTree.iter():
			if not self.elementExistsInList(elem.tag,self.xmlElementList):
				self.xmlElementList.append(elem.tag) 
		return
		
	@staticmethod
	def elementExistsInList(element ,list):
		for elem in list:
			if element == elem:
				return True
			else:
				continue
		return