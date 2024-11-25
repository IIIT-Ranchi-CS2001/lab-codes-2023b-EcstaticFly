namesList=[name for name in input().split()]
print(namesList)
rollNumberList=[roll for roll in input().split()]
print(rollNumberList)
MarksList=[int(marks) for marks in input().split()]
print(MarksList)
details=list(zip(namesList,rollNumberList,MarksList))
print(list(details))

afterSorted=sorted(details , key=lambda x:x[2])
print((afterSorted))
