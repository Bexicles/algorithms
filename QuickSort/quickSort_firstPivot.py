

def quickSort(A, n):

    if n == 1:
        return A

    else:

        pivot = getPivot(A, n)
        partition(A, pivot, n)

    return A


def getPivot(A, n):
    pivot = A[0]

    return pivot



def partition(A, pivot, n):

    l = A.index(pivot)
    i = l + 1

    for j in range(l, n):
        if A[j] < pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i +=1

    temp2 = A[l]
    A[l] = A[i-1]
    A[i-1] = temp2
    l = A.index(pivot)

    if len(A) == 2:
        return A

    else:
        B = A[0:l]
        len_B = len(B)
        C = A[l+1:n]
        len_C = len(C)


        if len_B > 0:
            A[0:l] = quickSort(B, len_B)

        if len_C > 0:
            A[l+1:n] = quickSort(C, len_C)

        return A


def runQuickSort(A):

    n = len(A)
    X = quickSort(A, n)

    return X


