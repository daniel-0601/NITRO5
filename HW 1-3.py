a=[1,2,3,4,5]
b=[]

c1=len(a)-1
c2=0   
           
while (c1>=0):
    b.insert(c2,a[c1])
    c1-=1
    c2+=1

print("a:",a)
print("reversed a:",b)

#for迴圈中無法對全域變數進行更動
#PS:python真的好奇怪