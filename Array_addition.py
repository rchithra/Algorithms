A = [1, 1, 0, 1]
B = [1, 0, 0, 1]
C = [None] * 5
carry = 0

for i in range((len(A) - 1), -1, -1):
    v = A[i] + B[i] + carry
    print("Values of ai {} and bi {} and c {}".format(A[i], B[i], carry))
    if v == 0:
        C[i + 1] = 0
        carry = 0
    if v == 1:
        C[i + 1] = 1
        carry = 0
    if v == 2:
        C[i + 1] = 0
        carry = 1
    if v == 3:
        C[i + 1] = 1
        carry = 1

C[0] = carry
print(C)
