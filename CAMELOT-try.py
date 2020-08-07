

import camelot
tables = camelot.read_pdf('C:\\Users\\E.H.PAUE\\python lessons\\Tablee.pdf') # write the path of the PDF file
tables
#<TableList n=1>

tables.export('meetingminutes.csv', f='csv', compress=True) # json, excel, html
tables[0]

#<Table shape=(7, 7)>

tables[0].parsing_report
#{
#    'accuracy': 99.02,
#    'whitespace': 12.24,
#    'order': 1,
#    'page': 1
#}

tables[0].to_csv('meetingminutes.csv') # to_json, to_excel, to_html

tables[0].df # get a pandas DataFrame!
