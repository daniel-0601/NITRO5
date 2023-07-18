info=[{ "name": "阿美", "phone": "0987-654321" },
      { "name": "小花", "phone": "0912-343531" },
      { "name": "安安", "phone": "0956-396471"}
      ]




while (1):
    x=input("What do you want to do ?")
    
    if(x=="add"):
        n=input("Please input a name :")
        p=input("Please input phone number XXXX-XXXXXX :")
        info.append({"name": n, "phone": p })
        print(info)
        
    elif(x=="find"):
        m=input("Please input name or nuber XXXX-XXXXXX :")
        for i in info:
            if (m==i['name']):
                print(i['phone'])
                break
            elif (m==i['phone']):
                print(i['name'])
                break
    elif(x=="printall"):
       for i in info:
           print(i['name'],':',i['phone'])
           
 