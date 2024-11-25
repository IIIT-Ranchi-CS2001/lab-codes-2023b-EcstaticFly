str=input()

dict={}
#
for char in str:
    if char in dict:
        dict[char]+=1
    else:
        dict[char]=1

for char,count in dict.items():
    print(f"{char}:{count}")    