import email
import imaplib

username = ' a1160azz@gmail.com'
password = ' Password@2Password@2'
mail= imaplib.IMAP4_SSL ("imap.gmail.com") # set less secure apps # https:\\www.google.com\setting/security/lesssecureapps
mail.login (username, password)
mail.select("inbox")
mail.list() # list folder
mail.select ("all")
mail.select("new")
mail.create("item2") # creat new folder
#result , date= mail.uid('search',None, "ALL")
data

print(mail.list())
print(mail.select ("all"))
print(mail.select("new"))
print(mail.create("item2"))
#print (result , date= mail.uid('search',None, "ALL"))
print (data)
