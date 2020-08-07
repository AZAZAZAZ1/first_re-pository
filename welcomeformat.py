
import xlsxwriter # import to creat and write in Excell sheet #__important__: the xlsxwriter is module that have morkbook class, and xlsxwriter object, and worksheet class

workbook = xlsxwriter.Workbook('C:\\Users\\E.H.PAUE\python lessons\\Welocmeformat2.xlsx')# creat Excel file in the path called Welcomeformat
worksheet = workbook.add_worksheet('sheta')# create worksheet called 'Sheta'.

# to format the text size color, ...
cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
cell_format.set_font_size(16)
cell_format.set_underline(2)
cell_format.set_align('center')
cell_format1 = workbook.add_format({'font_color': 'blue'})
cell_format1.set_align('center')


worksheet.write('A1', 'Name', cell_format) # write in the cell A1 : Name , and format the text as per cell_format
worksheet.write('B1', 'Department', cell_format) #write in the cell B1 :Department  , and format the text as per cell_format



#We can define the row and column width for excel cells by using worksheet.set_column function   [column:column].

worksheet.set_column('B1:B1', 60) # column B1 : B1 wedth is 60 
worksheet.set_column('B2:B5',60,cell_format1) #column B2 : B5 wedth is 60  with cell format 
worksheet.set_column('A1:A5', 20,cell_format1) #column A1 : A5 wedth is 20  with cell format 

# change the row hight:

worksheet.set_row(0, 20)  # Set the height of Row 1 to 20.

# it is only itterable data in python not in eacell sheet : it will not posted as table ! , the for loop will put it as atable!
#data is tuples( with lists)
data = ( 
     ['Rajendra', 'Hi, You are on SQLShack.com, refer to all SQL Server related contents.'], 
     ['Kashish','How do you get to see a physiotherapist?'], 
     ['Arun', 'I am a student of class 1 in Bookburn primary school.'], 
     ['Rohan','Are you a Bank Manager?'], 
 ) 
# the first cell at the top and left has index or row=0 ,and cloumn = 0. you have to define from where you need to post your data (iteration by for loop):

# the row = 1 and col=0 are the intial input to operate the for loop !

row = 1
col = 0
# in the below loop , we are calling the write "method" from Worksheet "class". the method is like a function and the argument is used in this case.(review vedio #60 in python bible)
# need to review O.O.P

for name, score in (data):
    worksheet.write(row, col, name)   #__very important__ #first iteration :write in (row=1,col=0) ,name will be data[0][0]. and score will be dtata[0][1] and they will be iterated once togather in each loop
        
    worksheet.write(row, col + 1, score)  # same the above
    row += 1
workbook.close()

print (data[0][0],data[0][1] )

# you can see the iterration using http://pythontutor.com/visualize.html#mode=display
