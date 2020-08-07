
Films = {
"Finding Dory":[3,5],
"Bourne" :[18,5],
"Tarazan":[15,5],
"Gost Busters":[12,5]
}

while True:
    choise = input("What film you want to see")
    if choise in Films:
        pass
    elif  choise not in Films:
        print("film is not avaiable")
    Age = int(input("what is your age").strip().title())
    if Age >= Films[choise][0]:
        pass
    elif Age <= Films[choise][0]:
        print(" your age not allow you to eneter the film , select another film")
    Required_tickets=int(input("how many tickets you want?").strip())
    if Required_tickets <= Films [choise][1]:
        pass
    elif Required_tickets > Films [choise][1]:
        print("the riquired number of tickets not avaiable ,the avaiable number = ",Films [choise][1],"kindly reduce the tickets , or select another film")
    confirm = input ("Do you want to proceed for payment? y/n").strip().lower()
    if confirm == "y":
        Films[choise][1]= ((Films[choise][1])-(Required_tickets))
        print("your tickets confirmed")
    else:
        print ("thank you , kindly select another film")

# note the indent and lines.
# note how to use elif , else .
            
            
                                    
                    
   
    
  
