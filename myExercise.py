import sys
with open(sys.argv[1]) as f:
    inputlist = f.read().splitlines()
inputs=[]
for line in (inputlist):
    line=line.replace(":", ",")
    line=line.split(",")
    inputs.append(line)
a=sys.argv[2].split(",")
name_list=[]
for b in inputs:
    name_list.append(b[0])
for i in a:
   try:
       if i not in name_list:
           print(i[5])
   except:
       print("No record of {x} was found!".format(x=i))
   for b in inputs:
        if i==b[0]:
            print("Name: {x}, University: {y}, {z}".format(x=b[0],y=b[1],z=b[2]))
            Valid=True
   if Valid==False:
        print("No record of {x} was found!".format(x=i))
            
    