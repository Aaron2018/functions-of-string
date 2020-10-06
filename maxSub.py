#this file finds all same subs between 2 strings
s1=input("please input a string: ")
s2=input("please input a string: ")
sList=list()
sList.append(s1)
sList.append(s2)


lenList=list()
lenList.append(len(s1))
lenList.append(len(s2))

maxSubLen=min(lenList)

curSubPos1=0
curSubPos2=0
curSubLen=1
counter=0
posEnd1=0
posEnd2=0
while curSubLen<=maxSubLen:
    while curSubPos1+curSubLen<=len(s1):
        if curSubPos1+curSubLen==len(s1):
            posEnd1=None
        else:
            posEnd1=curSubPos1+curSubLen
        while curSubPos2+curSubLen<=len(s2):
            if curSubPos2+curSubLen==len(s2):
                posEnd2=None
            else:
                posEnd2=curSubPos2+curSubLen
            if s1[curSubPos1:posEnd1]==s2[curSubPos2:posEnd2]:
                counter+=1
            curSubPos2+=1
        curSubPos1+=1
        curSubPos2=0
    curSubLen+=1
    curSubPos1=0
    curSubPos2=0

print(counter)