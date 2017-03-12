import inversions as inv


A = []

with open('./inversions.txt') as f:
    for line in f:
        A.append(int(line))

len = int(len(A))
print(A)
print("Length of A", len)


print(inv.count_inversions(A)[1])

