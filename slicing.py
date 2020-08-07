#get user e-mail
email = input("what is your e-mail?").strip()

#slice user name
user= email[0:email.index("@")]

#slice domain name
domain= email[(email.index("@")+(1)):]

#@
at1 = email.strip(domain)
at2= email.strip(user)
at=at1+at2
#format message
message= "this is your user : {0} ,and this is your domain : {1} ,and this is your e-mai : {2}".format(user,domain,email)

#display out message

print (user)

print (domain)

print (message)



