s=input('please input a string: ')
flag=True

for i in s:
    if i>'z' or i<'A':
        flag=False

print(flag)