import PyPDF2 # import

pdfFile = open('C:\\Users\\E.H.PAUE\\python lessons\\meetingminutes1.pdf' ,'rb') # open the file since the PDF is binary data
Reader =PyPDF2.PdfFileReader(pdfFile) # process our PDF
Reader.numPage # get how many pages in the PDF # you will get 19

page = reader.getPage(0) # to get a certain page "page object".
page.extractText()  # extract text from the selected certain page -that mentioned above-.

#!!! you can convert PDF image to text without program !!:
#https://www.youtube.com/watch?v=O9nfRXDrwA4
