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