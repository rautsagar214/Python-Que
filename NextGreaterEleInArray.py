# Input for the first array
n1 = int(input())
arr1 = list(map(int, input().split()))

n2 = int(input())
arr2 = list(map(int, input().split()))

res = []

for num in arr1:
    found = False
    greater = -1

    for i in range(n2):
        if arr2[i] == num:
            for j in range(i+1, n2):
                if arr2[j] > num:
                    greater = arr2[j]
                    found = True
                    break
            break

    res.append(greater)
print(res)

# inputs
# n1 = 3
# arr1 = 4 1 2
# n2 = 4
# arr2 = 1 3 4 2

# output
# -1 3 -1
