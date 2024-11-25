s=input("Enter the String: ")
p=s.split()
c=0
for word in p:
    if word.lower() == word.lower()[::-1]:
        c+=1
print(c)
