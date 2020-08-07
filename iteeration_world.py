
names = ("abo", "Ahmed","mutwali")
comp= ("Apple","Dell", "ADNOC")
zipped= list(zip (names, comp))

print (zipped)
       
# [('abo', 'Apple'), ('Ahmed', 'Dell'), ('mutwali', 'ADNOC')]

for a,b in zipped: # it will itterate the 2 variables togather once in each loop 
    print (a, b)
    
# abo Apple
# Ahmed Dell
# mutwali ADNOC
