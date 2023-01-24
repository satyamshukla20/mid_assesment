#[“name512”, “same1example”, “joy18full”] replace the digits from string inside list
#1st way
li=[ 'name512','same1example','joy18full' ]
newlist=[]
for str in li:
    for i in str:
       if i.isdigit():
           str=str.replace(i,'')
    newlist.append(str)
print(newlist)

#2nd way
print(["".join([i for i in st if not i.isdigit()]) for st in li])