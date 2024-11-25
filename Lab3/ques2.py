x=int(input("Enter the no.: "))
p=x
ans=0
while x>0:
    ans+=int(x%10)
    x=x/10

print(f"Sum of digits of {p} is {ans}")