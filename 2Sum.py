# Use print() to print to the console
n = int(input())
arr = list(map(int,input().split()))
target = int(input())

ans = False


if n<=0 or arr == []:
  print("-1")
else:
  for i in range(n):
    for j in range(i+1,n):
      if arr[i] + arr[j] == target:
        print(i, j)
        ans = True
        break
    if ans:
      break

  if not ans:
    print("-1")