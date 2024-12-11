n = int(input())
arr = list(map(int, input().split()))

MOD = 10**9 + 7
total_sum = 0

# Generate all contiguous subarrays and calculate the sum of their minimum values
for i in range(n):
    current_min = arr[i]
    for j in range(i, n):
        if arr[j] < current_min:
            current_min = arr[j]
        total_sum = (total_sum + current_min) % MOD

print(total_sum)
