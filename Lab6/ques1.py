def my_zip(name,id,points,strct):
    if strct is False:
        answer=list(zip(name,id,points))
        return answer
    else:
        if(len(name)!=len(id) or len(name)!=len(points) or len(id)!=len(points)):
            return None
        else:
            answer=list(zip(name,id,points))
            return answer
        

    
customerName=[i for i in input().split()]
customerId=[i for i in input().split()]
customerShoppingPoints=[int(i) for i in input().split()]
changer=True
answer=my_zip(customerName,customerId,customerShoppingPoints,changer)
if(answer):
    print(answer)
else:
    print("length of lists are not equal so no zipping")
    
    