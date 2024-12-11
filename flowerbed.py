size = int(input())
n = int(input())
flowerbed = list(map(int, input().split()))

count = 0  # Counter for number of new flowers planted

for i in range(size):
    if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == size - 1 or flowerbed[i + 1] == 0):
        flowerbed[i] = 1  # Plant a flower here
        count += 1  # Increment the counter
        if count >= n:  # If we have planted enough flowers
            print("true")
            break
else:
    if count >= n:
        print("true")
    else:
        print("false")
        