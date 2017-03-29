import statistics as stat


count = 0


def swap(A, a, b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp

    return A


def quicksort(A, l, r, n):

    if n == 1:
        return A

    else:
        pivot = get_pivot(A, l, r, n)
        A = partition(A, pivot, l, r, n)
        return A


def get_pivot(A, l, r, n):

    if n % 2 == 0:
        m = int((n/2)-1)
    else:
        m = int((n-1)/2)

    pivot = stat.median([A[l], A[m], A[r]])
    return pivot


def partition(A, pivot, l, r, n):
    p = A.index(pivot)
    A = swap(A, p, l)  # swap pivot to first element of array
    p = A.index(pivot)  # update pivot index to reflect new position
    i = p+1

    global count
    count += n - 1

    for j in range(p+1, n):
        if A[j] < pivot:
            A = swap(A, i, j)
            i += 1

    else:
        A = swap(A, p, i-1)  # move pivot to position of partition
        p = A.index(pivot)  # update pivot index
        len_1 = len(A[l:i-1])
        len_2 = len(A[i:r+1])

        print("A is now", A, "and pivot is", pivot)
        if len_1 > 1:
            print("Idx is", l, "to", i, "& new array is", A[l:i-1], "length", len_1)
            quicksort(A, l, i-1, len_1)  # recurse on 'first half' of array, i.e. values less than pivot

        if len_2 > 1:
            print("Idx is", i, "to", r, "& new array is", A[i:r+1], "length", len_2)
            quicksort(A, i, r, len_2)  # recurse on 'second half' of array, i.e. values greater than pivot

        return A


def run_quicksort(A):
    print("original array is", A)
    global count
    count = 0

    n = len(A)
    l = 0
    r = n-1

    A = quicksort(A, l, r, n)
    print("sorted array is", A, "& there were", count, "comparisons")

    return A, count



B = [9, 11, 10, 3, 1, 16, 5, 4]
run_quicksort(B)
