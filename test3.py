Films = {
"Finding Dory":[3,5],
"Bourne" :[18,5],
"Tarazan":[15,5],
"Gost Busters":[12,5]
}

while True:
    choise = input ("what film you want to see").strip().title()
    if choise in Films:
        print("your choice is avaiable")
    elif print("your choice is not avaiable, kindly select another film "):
        
        Age = int(input ("what is your age").strip().title())
        if Age >= Films[choise][0]:
            pass
        elif print ("your age is not suitable, select another film "):
                   
                     
            Required_tickets= int(input("how many tickets you want").strip())
            if Required_tickets <= Films[choise][1]:
                pass
            elif print("the number of required tickets are not available , the avaiable number ="):
            
                confirm= input ("Do you want to proceed for payement? y/n?").strip().lower()
                if confirm == "y":
                    Films[choise][1]= ((Films[choise][1])-(Required_tickets))
                    print ("your tickets confirmed")
                else:
                    print("thanks, kindly select again any other film")
