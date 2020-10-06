s=input("please input a string: ")
aA=ord('a')-ord('A')

for ord1 in range(ord('a'),ord('z')+1):
    s=s.replace(' '+chr(ord1),' '+chr(ord1-aA))

if s[0]>='a' and s[0]<='z':
    s=chr(ord(s[0])-aA)+s[1:]

print(s)