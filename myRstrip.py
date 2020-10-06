s=input("please input a string: ")
len1=len(s)

strip=input('please input a string need to be deleted from right: ')
while len(strip)>len1:
    strip=input('input a shorter one: ')

len2=len(strip)

if s==strip:  #delete all
    s=''

sTemp=""
while sTemp!=s:
    sTemp=s
    if s[len1-len2:]==strip:
        s=s[:len1-len2]
        len1-=1

print(s)