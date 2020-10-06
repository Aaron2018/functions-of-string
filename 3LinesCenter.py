s1=input("please input string1: ")
s2=input("please input string2: ")
s3=input("please input string3: ")

sList=list()
sList.append(s1)
sList.append(s2)
sList.append(s3)

len1=len(s1)
len2=len(s2)
len3=len(s3)
lenList=list()
lenList.append(len1)
lenList.append(len2)
lenList.append(len3)

width=max(lenList)

print('+',end='')
i=0
while i<width:
    print('-',end='')
    i+=1
print('+')

digBef=0
digAft=0
sTemp=''
fill=' '
for i,j in zip(sList,lenList):
    sTemp=i
    digBef=(width-j)//2
    digAft=(width-j)//2+(width-j)%2
    while digBef>0:
        sTemp=fill+sTemp
        digBef-=1
    while digAft>0:
        sTemp+=fill
        digAft-=1
    sTemp='|'+sTemp+'|'
    print(sTemp)

print('+',end='')
i=0
while i<width:
    print('-',end='')
    i+=1
print('+')