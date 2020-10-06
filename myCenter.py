s=input('please input string: ')
len1=len(s)

width=int(input('please input width: '))
while width<len1:
    width=int(input('please input width greater than length of string: '))

fill=input('please input fill: ')

digBef=(width-len1)//2
digAft=(width-len1)//2+(width-len1)%2

while digBef>0:
    s=fill+s
    digBef-=1

while digAft>0:
    s+=fill
    digAft-=1

print(s)