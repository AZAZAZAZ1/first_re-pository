known_users=["Alice", "Bob", "clare","Dan","Ema","fred","jorgy","Harry"]
print(len(known_users))
      
while True:
    print("Hi my name is Travid")
    name= input("what is your name").strip().capitalize()

# if the name in the known user list then there are 2 options (remove him or not)

    if name in known_users :
        print ("hellow {0}".format (name))
        remove=input("would you like to remove your name? y/n?").lower().strip()
        if remove == "y" or "yes":
            known_users.remove(name)
            print(known_users) 
        elif remove=="n" or remove=="no":
            print("no problem , you are welocme") 
# if the user name is not in the known list ,then there are 2 options (add him or not)                
    else:
        print ("hmm  {0} im not sure if i have met you yet".format(name))
        add_me = input("would you like to add you in the list?. y/n?").lower().strip()
        if add_me == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif add_me == "n":
            print ("no worry see you around")
