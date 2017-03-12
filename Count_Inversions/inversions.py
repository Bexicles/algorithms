
## FUNCTIONS ##

## split array in two using 'divide function' ##
def divide(X):

    pivot = int(len(X)/2)  ## using a 'pivot' where length / 2 is cast to an integer
    Left = []
    Right = []


    if pivot%2 == 0:
        Left = X[0:pivot]
        Right = X[pivot:]

    else:
        odd_pivot = int((len(X)-1)/2)
        Left = X[0:pivot]
        Right = X[pivot:]


    return Left, Right


## sort numbers and count inversions in a given array ##
def sort_and_count(X):
    n = int(len(X))
    no_inversions = 0

    if n == 1:
        return X, no_inversions

    elif n == 2:
        if X[0] > X[1]:
            temp = X[0]
            X[0] = X[1]
            X[1] = temp
            no_inversions += 1
        return X, no_inversions

    else:
        (X, no_inversions) = count_inversions(X)
        return X, no_inversions


## merge & count split inversions ##
def count_split_inv(X, Y):
    Z = []
    n = int(len(X))
    m = int(len(Y))
    max = 10000000000
    no_split_inversions = 0

    j = 0
    i = 0
    while i <= max:
        if i == n:
            for j in range (j, m):
                Z.append(Y[j])
            break
        if j == m:
            for i in range (i, n):
                Z.append(X[i])
            break
        elif X[i] < Y[j]:
            Z.append(X[i])
            i += 1
        else:
            Z.append(Y[j])
            j += 1
            no_split_inversions += n - i

    return Z, no_split_inversions





## METHOD ##

def count_inversions(X):

## split array X into two subarrays, Left & Right ##
    number_inversions = 0
    Left, Right = divide(X)
    (L, left_inversions) = sort_and_count(Left)
    number_inversions += left_inversions
    (R, right_inversions) = sort_and_count(Right)
    number_inversions += right_inversions
    (Z, no_split_inversions) = count_split_inv(L, R)
    number_inversions += no_split_inversions

    return Z, number_inversions

