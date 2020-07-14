A = [5, 3, 2, 6, 1, 4, 1]

for j in range(0, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] >= key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

print(A)

