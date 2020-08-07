
# to copy and extract paragraph from existing Word document to new file document :

import docx

def getText(filename): # file name is variable will be replaced by argument.
    doc = docx.Document(filename) # in order to open the exisiting word file
    fullText = [] # creat blank list in varaible called fullText
    for para in doc.paragraphs: # loop over all paragraph in the word object.
        fullText.append(para.text) # append each paragraph _in text format_ to the full test list [ ]
    return '\n'.join(fullText) # join all togather by new line.
        
print (getText ('C:\\Users\\E.H.PAUE\\python lessons\\demo5.docx')) # this is the arguement " file path and name"  tha will repalace the variable" file name" 

