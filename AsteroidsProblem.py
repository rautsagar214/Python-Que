n = int(input())
arr = list(map(int, input().split()))

res = []
for asteroid in arr:
    while res and asteroid < 0 < res[-1]:
        if res[-1] < -asteroid:
            res.pop()
            continue
        elif res[-1] == -asteroid:
            res.pop()
        break
    else:
        res.append(asteroid)

if res:
    print(*res)
else:
    print("Everything Destroyed")
