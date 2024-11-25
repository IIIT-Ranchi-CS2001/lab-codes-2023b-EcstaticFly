
a = tuple((int(x) for x in input("Enter Coordinte of First Point: ").split()))
print(a)
b = tuple((int(x) for x in input("Enter Coordinte of First Point: ").split()))
print(b)
distance=((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)**(1/2)
print(distance)