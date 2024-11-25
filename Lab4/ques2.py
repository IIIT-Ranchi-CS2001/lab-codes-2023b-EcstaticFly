n=[int(x) for x in input("enter no. seprated by spaces : ").split()]
print(n)

mean=sum(n)/len(n)
n.sort()
if len(n)%2==0:
    median=(n[len(n)//2]+n[(len(n)//2)-1])/2
else:
    median=n[len(n)//2]


f = {}
for num in n:
    f[num] = f.get(num, 0) + 1

max_count = max(f.values())
mode = [num for num, count in f.items() if count == max_count]

print(f"mean is {mean}")
print(f"median is {median}")
print(f"mode is {mode}")
