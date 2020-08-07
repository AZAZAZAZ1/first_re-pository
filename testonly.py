Try= [[1,2,3],[4,5,6],[7,8,9]]

for x,y,z in Try:
    print (x)
    print (x,y)
    print (x,y,z)
    
print ('------------------------------------------------------')

Try1= ([1,2,3],[4,5,6],[7,8,9])
for x,y,z in Try:
    print (x)
    print (x,y)
    print (x,y,z)

print ('------------------------------------------------------')

Try1= ((1,2,3),(4,5,6),(7,8,9))
for x,y,z in Try:
    print (x)
    print (x,y)
    print (x,y,z)

print ('############################################')

Try= [[1,2,3],[4,5,6],[7,8,9]]

for x,y in Try:
    print (x)
    print (x,y)
    
print ('------------------------------------------------------')

Try1= ([1,2,3],[4,5,6],[7,8,9])
for x,y in Try:
    print (x)
    print (x,y)

    
print ('------------------------------------------------------')

Try1= ((1,2,3),(4,5,6),(7,8,9))
for x,y in Try:
    print (x)
    print (x,y)

print ('-------------------------------')

data = ( 
     ['Rajendra', 'Hi, You are on SQLShack.com, refer to all SQL Server related contents.'], 
     ['Kashish','How do you get to see a physiotherapist?'], 
     ['Arun', 'I am a student of class 1 in Bookburn primary school.'], 
     ['Rohan','Are you a Bank Manager?'], 
 ) 

row = 1
col = 0


for name, score in (data):
    worksheet.write(row, col, name)   #__very important__ #first iteration :write in (row=1,col=0) the name is unpacked arguments  write(row, col, *args). *args: means unpacked :refer to vedio 61 python bible
    
    worksheet.write(row, col + 1, score)  # write(row, col, *args)- unpacked argument
    row += 1
workbook.close()
































    
