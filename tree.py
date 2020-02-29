
def solution(A):
    last_val = A[0]
    i = 1
    while i < len(A):
        if A[i] < last_val:
            return 2 if (i == len(A) - 1 or A[i+1] >= last_val) else 1
        last_val = A[i]
        i = i + 1


A = [3, 4, 5, 4]
test = solution(A)
print(test)
