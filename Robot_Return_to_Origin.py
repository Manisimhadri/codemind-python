s=input()
c=0
for i in s:
    if i=='U' or i=='R':
        c+=1
    if i=='L' or i=="D":
        c-=1

if c==0:
    print("True")
else:
    print("False")