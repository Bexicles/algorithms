

def QuickSort(A, n):

    if n == 1:
        return A

    else:
        pivot = A[0]

        Partition(A)

    return





def Partition(A, pivot, n):


    l = (A.index[pivot])
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


    B = A[pivot+1:i]
    len_B = len(B)
    C = A[i:j-1]
    len_C = len(C)

    QuickSort(B,len_B)
    QuickSort(C, len_C)



def RunQuickSort(A, n):

    X = QuickSort(A, n)

    return X