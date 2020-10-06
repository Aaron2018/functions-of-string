s=input("please input a string: ")
len1=len(s)

sub=input("please input a sub: ")
while len(sub)>len1:
    sub=input("please input a sub which length is less than string: ")
len2=len(sub)

curPos=0    #current position
slice1=''
counter=0
while curPos<len1:
    slice1=s[curPos:curPos+len2]
    if slice1==sub:
        counter+=1
    curPos+=1

print(counter)