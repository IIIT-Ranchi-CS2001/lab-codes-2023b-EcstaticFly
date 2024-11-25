def bubble_sort(lst,l):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j][l] > lst[j+1][l]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
def my_sort(inputList,key):
    if key==0:
        bubble_sort(inputList,0)
    elif key==1:
        bubble_sort(inputList,1)
    else:
        bubble_sort(inputList,2)
    return inputList
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
changer=False
answer=my_zip(customerName,customerId,customerShoppingPoints,changer)
if(answer):
    print(answer)
else:
    print("length of lists are not equal so no zipping")
    
    
key=2
finalSortedList=my_sort(answer,key)
print(finalSortedList)