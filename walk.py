import os

for x,y,z in os.walk('C:\\Users\\E.H.PAUE\\Desktop\\building 2020\\home design'):
	print('the folder is'+ x)
	print('the sub folder in '+x+'are:'+str(y))
	print('the filenames in'+x+'are:'+str(z))
	print()
