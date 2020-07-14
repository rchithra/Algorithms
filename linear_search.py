A = [5,3,2,6,1,4]
v = int(input("Enter the value: "))
found = 'Nil'
for i in range (0, len(A)):
    if A[i] == v :
        found = i
        break
print(found)
 
A1 = [5,3,2,6,1,4]
i = 0
found1 = 'Nil'
while (i < len(A1) and found1 == 'Nil'):
    if A1[i] == v:
        found1 = i
    i = i + 1
print (found1)



