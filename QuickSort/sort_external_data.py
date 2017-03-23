import QuickSort.quickSort_firstPivot as QS

A = []

with open('./quickSort.txt') as f:
    for line in f:
        A.append(int(line))

len = int(len(A))
print("Length of A", len)

print(QS.runQuickSort(A))

