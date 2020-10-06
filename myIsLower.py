s=input("please input a string: ")
flag=True

for i in s:
    if i<'a' or i>'z':
        flag=False

print(flag)