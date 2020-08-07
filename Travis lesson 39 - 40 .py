# Travis - vedio 40 correct command:
Known_users=["Alice","Bob","Claire","Dan","Emma","Fred","Gerogio","Harry"]


while True:
    print("this is users after loop", Known_users)
    print("Hi My name is Travis")
    name = input("What is your name?").strip().capitalize()
    
# if the name in the list of knowon users (you can remove and not remove):
    if name in Known_users:
        print("Hello {}".format(name))
        remove = input("would you like to be removed from the system ?(y/n)").lower().strip()

        if remove == "y" :
            print (Known_users)
            Known_users.remove(name)
            print (Known_users)
        elif remove == "n" : # note if you write no , non , nooooooooooo , it will work because "n" is included in these words.
            print ("no problem , i dont you to leave any way")
        
           # note : if you press yes , then alice will be removed from list,
           #and it will not one of the known perople in the list.in the second loop the program will ask
           #if she need to be added to the list.if she say no , this she will still out of list (in the third loop).
           # if you press CTL +C , the program will be started ,and the alice will be in the list (the Known_users will be set as orginal list)
           #note: elif remove == "n" or "no" , then python will evaluate False or True = True.(this will not your system work propely.
            
# if the name is not in the list of the known users:(you can add or not add)            
    else:
        print("Hmmm idont think i have met you yet {}".format(name))
        add_me = input ("wouldyou like me to add you in the system? y/n").strip().lower()
        if add_me == "y":
            print (Known_users)
            Known_users.append(name)
            print (Known_users)
        elif add_me == "n":
            print ("no worries , see you around")
            
            
