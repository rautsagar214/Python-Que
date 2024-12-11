n = int(input())
arr = list(map(int, input().split()))
k = int(input())

max_vals = []

for i in range(n - k + 1):
    max_val = max(arr[i:i + k])
    max_vals.append(max_val)

if max_vals:
    print(max_vals)
else:
    print("1")
