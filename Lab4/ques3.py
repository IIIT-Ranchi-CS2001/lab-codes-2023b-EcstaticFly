
p=[courseName for courseName in input().split()]
q=[courseCode for courseCode in input().split()]
r=[]
for i in range(len(p)):
    r.append(p[i]+":"+q[i])
print(r)


