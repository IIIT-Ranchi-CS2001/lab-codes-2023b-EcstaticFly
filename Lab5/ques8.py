# here we are using bubble sort for sorting not any built in functions like sort, sorted

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j][2] > lst[j+1][2]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
customerName=[i for i in input().split()]
print(customerName)
customerId=[i for i in input().split()]
print(customerId)
customerShoppingPoints=[int(i) for i in input().split()]
print(customerShoppingPoints)


# list of tuples using zip
customerDetails=zip(customerName,customerId,customerShoppingPoints)
print(list(customerDetails))

# list of tuples without using built in function zip
customerResult=[(customerName[i],customerId[i],customerShoppingPoints[i]) for i in range(min(len(customerName),len(customerId),len(customerShoppingPoints)))]
print(customerResult)

bubble_sort(customerResult)

print(customerResult)