firstPoint= [int(x) for x in input().split()]
print(firstPoint)
secondPoint= [int(x) for x in input().split()]
print(secondPoint)

a=(firstPoint[0]-secondPoint[0])
b=(firstPoint[1]-secondPoint[1])
if a==0:
    print(f"x = {firstPoint[0]}")
elif b==0:
    print(f"y = {firstPoint[1]}")
else:
    constant=(firstPoint[1]-(firstPoint[0]/(a/b)))
    print(f"y = {a/b}x + {constant}")