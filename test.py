b=8
a=8
count=0
while b>0:
    t=a
    a=b
    b=t%b
    count=count+1
print(count)    