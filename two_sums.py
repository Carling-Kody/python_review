



def find_target(A, target):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] + A[j] == target:
                print(i, j)
                return [i, j]

def main():

    A = [2, 7, 11, 15]
    target = 17
    find_target(A,target)
main()
