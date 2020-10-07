s=input("please input a string: ")
flag=True
sLen=len(s)

fowardStart=0
fowardEnd=sLen//2
if sLen%2==0:
    reverseStart=sLen//2-1
else:
    reverseStart=sLen//2

#for i,j in zip(s[fowardStart:fowardEnd],s[:reverseStart:-1]):
#    if flag==False: break
#    if i!=j:
#        flag=False
#        break

if s[fowardStart:fowardEnd]!=s[:reverseStart:-1]:
    flag=False

print(flag)