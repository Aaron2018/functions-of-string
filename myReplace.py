s=input("please input a string: ")
old1=input("please input old string: ")
new1=input("please input new string: ")
counter=int(input("please input counter: "))

oldLen=len(old1)
newLen=len(new1)
sLen=len(s)
curPos=0
curCounter=0

while curPos+newLen<=sLen:
    if s[curPos:curPos+oldLen]==old1:
        s=s[0:curPos]+new1+s[curPos+oldLen:]
        sLen=len(s)
        #curPos-=1
        curCounter+=1
    curPos+=1
    if curCounter>counter:
        break

print(s)