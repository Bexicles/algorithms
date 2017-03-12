
## FUNCTIONS ##

## split array in two using 'divide function' ##
def divide(X):

    pivot = int(len(X)/2)  ## using a 'pivot' where length / 2 is cast to an integer
    Left = []
    Right = []


    if pivot%2 == 0:
        Left = X[0:pivot]
        Right = X[pivot:]

    print(Left, Right)
    return Left, Right


## sort numbers and count inversions in a given array ##
def sort_and_count(X):
    n = int(len(X))
    no_inversions = 0

    if (n == 2):
        if (X[0] > X[1]):
            temp = X[0]
            X[0] = X[1]
            X[1] = temp
            no_inversions+1
    else:
        inversions(X)

    return X, no_inversions


## merge & count split inversions ##
def count_split_inv(X, Y):
    Z = []
    n = int(len(X))
    no_split_inversions = 0

    j = 0
    i = 0
    m = 0
    while m <= 1000:
        if( X[i] < Y[j]):
            Z.append(X[i])
            m = m+1
            i = i+1
            print("Z is ",Z)
            print("m is ", m)
        else:
            Z.append(Y[j])
            m = m+1
            j = j+1
            print("Z is ",Z)
            print("m is ", m)
            no_split_inversions = no_split_inversions + (n - i)

    print("Z equals ", Z)
    print("split inversions = ", no_split_inversions)
    return Z, no_split_inversions




## METHOD ##

def inversions(X):

## split array X into two subarrays, Left & Right ##
    number_inversions = 0
    Left, Right = divide(X)
    (Left, no_inversions) = sort_and_count(Left)
    number_inversions = number_inversions + no_inversions
    (Right, no_inversions) = sort_and_count(Right)
    number_inversions = number_inversions + no_inversions
    (Z, no_split_inversions) = count_split_inv(Left, Right)
    number_inversions = number_inversions + no_split_inversions
    print(Z)
    print(number_inversions)



A = [1, 3, 4, 2]
inversions(A)
