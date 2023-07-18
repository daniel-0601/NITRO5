a=[]

print("input number")

count=0
while (count < 5):
    b=input()
    b=int(b)
    a.insert(count,b)
    count += 1
    
print(a)

for i in range(0, 4):
    dif = a[i+1]-a[i]
    if dif==1:
        i+=1
    else:
        for j in range(1, dif):
            print(a[i]+j)
            j+=1
        i+=1