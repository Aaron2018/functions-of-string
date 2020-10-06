s=input("please input a string: ")
sWoSpc=''   #string without space

pos1=0  #start position of string
pos2=0  #end position of string
curPos=0
for i in s:
    if pos1==0 and i!=' ':
        pos1=curPos
    if pos1!=0 and i!=' ':
        pos2=curPos
    curPos+=1

sWoSpc=s[pos1:pos2+1]   #到pos2+1索引结束,但是不包括pos2+1
print(sWoSpc)