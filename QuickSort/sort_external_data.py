from quicksort_pivot_median import run_quicksort


A = []

with open('./quicksort.txt') as f:
    for line in f:
        A.append(int(line))

len = int(len(A))
print("Length of A", len)

print(run_quicksort(A)[1])

