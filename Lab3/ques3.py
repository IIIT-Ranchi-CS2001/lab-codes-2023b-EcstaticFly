a=int(input())

i=1
j=1
k=3
print("Fibonacci Series: \n0\n1\n1")

while k<a:
    print(i+j)
    temp=j
    j=i+j
    i=temp
    k+=1