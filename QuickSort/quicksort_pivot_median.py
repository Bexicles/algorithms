import statistics as stat


count = 0


def quicksort(A, n):

    if n == 1:
        return A

    else:
        pivot = get_pivot(A, n)
        A = partition(A, pivot, n)
        return A


def get_pivot(A, n):

    if n%2 == 0:
        m = int((n/2)-1)
    else:
        m = int((n-1)/2)

    pivot = stat.median([A[0], A[m], A[n-1]])
    return pivot



def partition(A, pivot, n):
    l = A.index(pivot)
    temp2 = A[l]  # swap pivot to first element of array
    A[l] = A[0]
    A[0] = temp2
    l = A.index(pivot)  # update pivot index to reflect new position

    i = 1

    global count
    count += n - 1

    for j in range(l, n):
        if A[j] < pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1

    temp2 = A[l]
    A[l] = A[i - 1]
    A[i - 1] = temp2
    l = A.index(pivot)

    if len(A) == 2:
        return A

    else:
        len_B = len(A[0:l])
        len_C = len(A[l+1:n])

        if len_B > 0:
            A[0:l] = quicksort(A[0:l], len_B)

        if len_C > 0:
            A[l+1:n] = quicksort(A[l+1:n], len_C)

        return A


def run_quicksort(A):
    print("original array is", A)
    global count
    count = 0

    n = len(A)

    A = quicksort(A, n)
    print("sorted array is", A, "& there were", count, "comparisons")

    return A, count



B = [3, 20, 12, 14]
run_quicksort(B)
