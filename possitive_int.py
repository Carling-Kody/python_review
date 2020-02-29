
def solution(A):
    num = ""
    for i in range(1, len(A)+1):
        if not i in A:
            num = i
            break
        else:
            num = len(A)+1
    print(num)
    return num


# should return 5
# A = [1, 3, 6, 4, 1, 2]
# should return 4
#  = [1, 2, 3]
# should return 1
A = [-1, -3, 1, 2, 3, 0, 6, 4, 5]
# n = len(a)

solution(A)
