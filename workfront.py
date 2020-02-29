


def solution(N):
    num_check = 0
    half = 0
    boom = []
    my_neglist = []
    if N % 2 == 0:
        num_check = N
        half = int(num_check/2)
        for i in range(1, half+1):
            boom.append(i)
        my_neglist = [-x for x in boom]
        my_list = boom + my_neglist
    else:
        num_check = N - 1
        half = int(num_check/2)
        for i in range(0, half+1):
            boom.append(i)
        my_neglist = [-x for x in boom]
        list_dup = boom + my_neglist
        my_list = list(set(list_dup))
    return my_list


N = 100
test = solution(N)
print(test)
