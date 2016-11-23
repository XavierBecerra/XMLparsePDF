#!/usr/bin/python
import os

from TEXhandler import TEXhandler 
from XMLhandler import XMLhandler 
from LatexTex import *

XMLmanager = XMLhandler() #This object manages the XML source file to be parsed
TEXmanager = TEXhandler() #This object manages the TEX file that will be used to create the ATM pdf
TEXsource = TEXhandler()  #This object manages other TEX files 

NAME_BASE = "ATM-ATA"
XML_TYPE = ".xml"
TEX_TYPE = ".tex"
PDF_TYPE = ".pdf"

def main():


	#select ATM to be parsed
	while XMLmanager.xmlTree == 0:
		atm_name = requestUserDesiredDocument()
		XMLmanager.setXMLfileToBeParsed( atm_name + XML_TYPE )
	
	XMLmanager.getListOfTagsInXML()
	TEXmanager.openAndCreateTexFile( atm_name + TEX_TYPE )
	
	prepareTexDocumentBeforeParsing()
	
	iterateThroughATM()
	
	finalizeTexDocumentBeforeExiting()
	
	TEXmanager.closeTexFile()
	
	os.system("pdflatex "+ atm_name + TEX_TYPE)
	
	
	return
	
def requestUserDesiredDocument():

	printSelectionMenuOnScreen()
	selectedATA = captureRequest()
	
	return NAME_BASE + selectedATA

def printSelectionMenuOnScreen():

	print( "select existing ATM-ATA number. \n")
	return

def captureRequest():
	try:
		capture=input('ATA number:')
	except:
		print("Error occured. Input lost")
		capture = ""
	return capture

def prepareTexDocumentBeforeParsing():
	insertHeather()
	insertDocumentTitle()
	beginTexDocument()
	makeTitle()	

def insertHeather():
	TEXsource.openReadOnlyTexFile( "ATM_header" + TEX_TYPE )	
	for line in TEXsource.texFile:
		TEXmanager.writeTextToTexFile(line)
	TEXsource.closeTexFile()
	return
	
def insertDocumentTitle():
	title = getCoverDefinition(TEXmanager.getName() )
	TEXmanager.writeTextToTexFile(title)
	return
	
def finalizeTexDocumentBeforeExiting():
	string = getEndDocumentCommnad()
	TEXmanager.writeTextToTexFile(string)
	
def beginTexDocument():
	string = getBeginDocumentCommnad()
	TEXmanager.writeTextToTexFile(string)
	
def makeTitle():
	string = getMakeTitleCommnad()
	TEXmanager.writeTextToTexFile(string)

def iterateThroughATM():

	print(XMLmanager.xmlPosition)
	for child in XMLmanager.xmlPosition:
		XMLmanager.xmlPosition = child
		testName = wrapTestLevelText(XMLmanager.xmlPosition.get("NAME"))
		TEXmanager.writeTextToTexFile(testName)
		print(XMLmanager.xmlPosition.tag)
		for child in XMLmanager.xmlPosition:
			XMLmanager.xmlPosition = child
			if child.tag == "action":
				ActionText = wrapActionLevelText(XMLmanager.xmlPosition.text)
				TEXmanager.writeTextToTexFile(ActionText)
			print("   " + XMLmanager.xmlPosition.tag)
			for child in XMLmanager.xmlPosition:
				XMLmanager.xmlPosition = child
				if child.tag == "verification":
					VerificationText = wrapVerificationLevelText(XMLmanager.xmlPosition.text)
					TEXmanager.writeTextToTexFile(VerificationText)
			
	return
	
def wrapTestLevelText(text):
	apendedText = "THIS IS A TEST NAME:  " + text + "\n \n "
	return apendedText
	
def wrapActionLevelText(text):
	apendedText = "           Action to perform:   " + text + "\n \n "
	return apendedText
	
def wrapVerificationLevelText(text):
	apendedText = r"\CheckBox[]{" + text + r"}"+ " \n \n" + getVerificationForm(text)
	return apendedText
	
main()