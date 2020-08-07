# cinnema 2 : another way to make the program:

Films = {
"Finding Dory":[3,5],
"Bourne" :[18,5],
"Tarazan":[15,5],
"Gost Busters":[12,5]
}
while True:
    choice = input("what film you want to see?").strip().title()
    if choice in Films:
        Age= int(input("How old are you").strip())
        if Age >= Films[choice][0]:
            num_seats= Films[choice][1]
            if num_seats>0:
                print("Enjoy the fil")
                Films[choice][1]= Films[choice][1]-1
            else:
                print ("sorry, we are sold out")
                                    
               
        else:
            print("you are too young")
    else:
        print("we dont have the film")
                 
# kindly note the syntax and lines and how the program excuted.
