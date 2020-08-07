import random

class Pound:
    value=1
    colour="gold"
    num_edges=1
    diameter= 22.5
    thickness=3.15
    heads=True
coin1=Pound()
x= print(coin1.value)

#=============================

class Pound:

    def __init__(self,rare=False):
        self.value=1
        self.colour="gold"
        self.num_edges=1
        self.diameter= 22.5
        self.thickness=3.15
        self.heads=True
        
        self.rare=rare
        if self.rare:
            self.value=1.25
        else:
            self.value=1
    def rust(self):
        self.colour="greenish"
    def clean (self):
        self.colour="gold"
    def flip(self):
        heads_options=[True,False]
        choice=random.choice(heads_options)# refer to random lesson
       
        self.heads=choice
        
    def __del__(self):#destructor
        print('coin spent')
        # del coin1 will give you : coin spent

        
coin1=Pound()
x= print(coin1.value)
        
