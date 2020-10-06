s=input("please input a string: ")
flag=True

for i in s:
    if i<'A' or i>'Z':
        flag=False

print(flag)