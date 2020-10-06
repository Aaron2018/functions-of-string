s=input("please input a string: ")
aA=ord('a')-ord('A')

for ord in range(ord('a'),ord('z')+1):
    s=s.replace(chr(ord),chr(ord-aA))

print(s)