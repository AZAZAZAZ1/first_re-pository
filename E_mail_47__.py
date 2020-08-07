import imapclient
import pyzmail36

conn = imapclient.IMAPClient('imap.gmail.com',ssl=True) # make connection to gmail server

conn.login('a1160azz@gmail.com','Password@2Password@2') # log in to the e-mail suing python 
# #result   :   a1160azz@gmail.com authenticated (Success)'

conn.select_folder('INBOX',readonly = True)
print(conn.select_folder('INBOX',readonly = True))
#result   :   'PERMANENTFLAGS': (), b'FLAGS': (b'\\Answered', b'\\Flagged', b'\\Draft', b'\\Deleted', b'\\Seen', b'$NotPhishing', b'$Phishing'), b'UIDVALIDITY': 635669701, b'EXISTS': 52877, b'RECENT': 0, b'UIDNEXT': 59304, b'HIGHESTMODSEQ': 4760899, b'READ-ONLY': [b'']}

print('#___________________________________________________#')

# to get all the ID of e-mails that sent TO : a1160azz@gmail.com

messages = conn.search(['TO', 'a1160azz@gmail.com'])
print(conn.search(['TO', 'a1160azz@gmail.com']))

print('#___________________________________________________#')


# to get all the ID of e-mails that FROM : a1160azz@gmail.com

messages = conn.search(['FROM', 'a1160azz@gmail.com'])
print(conn.search(['FROM ', 'a1160azz@gmail.com']))

print('#___________________________________________________#')


for msgid, data in conn.fetch(messages, ['ENVELOPE']).items():
    envelope = data[b'ENVELOPE']

print(data)

print(envelope)

print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))

print('#___________________________________________________#')

#pyzmail36.PyzMessage.factory(rawMessage[


conn.logout(),

# refernce :  https://imapclient.readthedocs.io/en/2.1.0/


#UIDs = conn.search(['SINCE 20-Apr-2020']) # you can change these UIDs to emails using the below fetch method
#UIDs
#conn.fetch( --

# pyzmail36.PyzMessage.factory(rawMessage[47474][

# this lesson need specialist and new toyotorial.

#_____________________________

#import email
#import imaplib

#username = ' a1160azz@gmail.com'
#password = ' Password@2Password@2'
#mail= imaplib.IMAP4_SSL ("imap.gmail.com") # https:\\www.google.com\setting/security/lesssecureapps
#mail.login (username, password)
#mail.select("inbox")



