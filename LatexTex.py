def getCoverDefinition(titleName):
	string = (r'\title{' + ' \n' 
	r'\includegraphics[width=5.75in]{Simteq-ISS.png} \\' + ' \n' 
	r'\vspace*{1in}' + ' \n' 
	r'\textcolor{BrickRed}{\fontsize{40}{50}\selectfont Acceptance Test Manual} \vspace{0.5em}\\ \fontsize{30}{40}\selectfont ' + titleName +'} \n' 
	r'\author{Author 1 (Author 1)\\' + ' \n' 
	r'\vspace*{0.5in} \\' + ' \n'  
	r'\textbf{Simteq B.V.}\\' + ' \n' 
	r'Vijfhuizen, The Netherlands' + ' \n' 
	r'} \date{\today} ' + ' \n' 
	r'%--------------------Make usable space all of page' + ' \n' 
	r'\setlength{\oddsidemargin}{0in} \setlength{\evensidemargin}{0in}' + ' \n' 
	r'\setlength{\topmargin}{0in}     \setlength{\headsep}{-.25in}' + ' \n' 
	r'\setlength{\textwidth}{6.5in}   \setlength{\textheight}{8.5in}' + ' \n' 
	r'%--------------------Indention' + ' \n' 
	r'\setlength{\parindent}{1cm}' + ' \n')
		
	return string

def getVerificationForm(text):	
	string = (r'\begin{Form}' + ' \n' + text + ' \n'
    r'\CheckBox[bordercolor={0 0 0},height=1ex,width=1.5ex, name=ch1]{Yes}\quad' + ' \n'
    r'\CheckBox[bordercolor={0 0 0},height=1ex,width=1.5ex, name=ch2]{No}\quad' + ' \n'
	r'\end{Form}' + ' \n')
	return string
	
def getEndDocumentCommnad():
	string = r'\end{document}'+ ' \n'
	
	return string
	
def getBeginDocumentCommnad():
	string = r'\begin{document}' + ' \n' 
	
	return string
	
def getMakeTitleCommnad():
	string = r'\maketitle'+ ' \n'  #prefix r is used to get  a raw \ 
	
	return string