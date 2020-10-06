s=input('please input a string:')
flag=True

for i in s:
    if i<'0' or i>'9':
        flag=False

print(flag)