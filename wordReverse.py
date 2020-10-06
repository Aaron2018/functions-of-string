s=input("please input a string: ")
len1=len(s)

spcPos1=-1   #space position
spcPos2=-1
curPos=-1
newS=''

for i in s[::-1]:
    if i==' ':
        spcPos1=curPos
        if spcPos2==-1:
            newS=newS+s[spcPos1+1:]+' '
        else:
            newS=newS+s[spcPos1+1:spcPos2]+' '
        spcPos2=spcPos1
    if curPos==-len1:
        newS=newS+s[:spcPos1]
    curPos-=1

print(newS)