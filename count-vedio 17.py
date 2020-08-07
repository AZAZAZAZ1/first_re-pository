message= "it was a bright cold day in April, and the clocks were striking thirteen"
count ={}
for charter in message:
    count.setdefault(charter,0)
    count[charter]=count [charter]+1
print(count)
