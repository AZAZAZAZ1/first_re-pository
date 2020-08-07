

import random
class Coin:
    def __init__(self,rare=False,clean=True,heads=True,**kwargs):#Kwargs is to back in dictionary the upacked ** data

        for key,value in kwargs.items():
            setattr(self,key,value)



        self.is_rare=rare
        self.is_clean=clean
        self.heads=heads
        

        if self.is_rare:
            self.value=self.original_value*1.25
        else:
            self.value=self.original_value
        if self.is_clean:
            self.colour=self.clean_colour
        else:
            self.colour=self.rusty_colour
        
    def rust(self):
        self.colour=self.rusty_colour
        
    def clean(self):
        self.colour=self.clean_colour
        
    def __del__(self):#destructor
        print('coin spent')
    def flip(self):
         heads_options=[True,False]
         choice=random.choice(heads_options)
    def __str__(self):
        if self.orginal_value>=1:
            return"{} coin".format(int(self,original_value))
        else:
            return"{}p coin".format(int(self.original_value*100))
#==================================================
        
class One_pence(Coin):
    def __init__(self):
        data={
            "original_value":0.01,
            "clean_colour":'bronze' ,
            "rusty_colour":'brownesh',
            "num_edges":1,
            "diameter":20.3,
            "thickness":1.52,
            "mass":3.56
            }
        super().__init__(**data)
#=================================================
class Two_pence(Coin):
    def __init__(self):
        data={
            "original_value":0.02,
            "clean_colour":'bronze' ,
            "rusty_colour":'brownesh',
            "num_edges":1,
            "diameter":25.9,
            "thickness":1.85,
            "mass":7.12
            }
        super().__init__(**data)
#===================================================
class Five_pence(Coin):
    def __init__(self):
        data={
            "original_value":0.05,
            "clean_colour":'silver' ,
            "rusty_colour":None,
            "num_edges":1,
            "diameter":18.0,
            "thickness":1.77,
            "mass":3.25
            }
        super().__init__(**data)
# because the silver is not rusting:
    def rust (self):
        self.colour=self.clean_colour
        def clean(self):
            self.colour=self.clean_colour

#======================================================================

class Ten_pence(Coin):
    def __init__(self):
        data={
            "original_value":0.10,
            "clean_colour":'silver' ,
            "rusty_colour":None,
            "num_edges":1,
            "diameter":24.5,
            "thickness":1.85,
            "mass":6.5
            }
        super().__init__(**data)
# because the silver is not rusting:
    def rust (self):
        self.colour=self.clean_colour
    def clean(self):
        self.colour=self.clean_colour

#====================================================================

class Twenty_pence(Coin):
    def __init__(self):
        data={
            "original_value":0.20,
            "clean_colour":'silver' ,
            "rusty_colour":None,
            "num_edges":7,
            "diameter":21.4,
            "thickness":1.7,
            "mass":5
            }
        super().__init__(**data)
# because the silver is not rusting:
    def rust (self):
        self.colour=self.clean_colour
    def clean(self):
        self.colour=self.clean_colour
    
#====================================================================

class Fifty_pence(Coin):
    def __init__(self):
        data={
            "original_value":0.50,
            "clean_colour":'silver' ,
            "rusty_colour":None,
            "num_edges":7,
            "diameter":27.3,
            "thickness":1.78,
            "mass":8
            }
        super().__init__(**data)
# because the silver is not rusting:
    def rust (self):
        self.colour=self.clean_colour
    def clean(self):
        self.colour=self.clean_colour

#====================================================================

class Two_pound(Coin):
    def __init__(self):
        data={
            "original_value":2,
            "clean_colour":'gold&silver' ,
            "rusty_colour":'greenesh',
            "num_edges":1,
            "diameter":28.4,
            "thickness":2.5,
            "mass":12.00
            }
        super().__init__(**data)


#================================================================ 
class One_pound(Coin):
    def __init__(self):
        data={
            "original_value":1,
            "clean_colour":'gold' ,
            "rusty_colour":'greenesh',
            "num_edges":1,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5
            }
        super().__init__(**data) # super is used to get all parent class data inorder to avoide override by the child class. note: [parent class can be in another library] .**data:umpack keyword argument
            
            
#=================================================================
coins=[One_pence,Two_pence, Five_pence,Ten_pence, Twenty_pence, Fifty_pence, One_pound, Two_pound]
for coin in coins:
    arguments=[coin, coin.colour,coin.value, coin.diameter, coin.thickness, coin.num_edges,coin.mass]
    string= "{}.colour:{}, value{},diameter(mm):{}, thickness(mm):{},number of edges:{}, mass(grams):{}".format(*arguments)
    

#=====================================================================
    #def __init__(self,rare=False):
        
        #self.value=1
        #self.colour="gold"
        #self.num_edges=1
        #self.diameter= 22.5
        #self.thickness=3.15
        #self.heads=True
        
        #self.rare=rare
        #if self.rare:
            #self.value=1.25
        #else:
            #self.value=1
    #def rust(self):
        #self.colour="greenish"
    #def clean (self):
        #self.colour="gold"
    #def flip(self):
        #heads_options=[True,False]
        #choice=random.choice(heads_options)# refer to random lesson
       
        #self.heads=choice
        
    #def __del__(self):#destructor
        #print('coin spent')
        ## del coin1 will give you : coin spent

        
#coin1=Pound()
#x= print(coin1.value)
        
