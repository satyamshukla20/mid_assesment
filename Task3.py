#[1,2,3,1,3,4,6,5,3] get unique numbers from list with basic constructs
li=[1,2,3,1,3,4,6,5,3]
dict={}
for i in li:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
        
print([k for k,v in dict.items() if v==1])