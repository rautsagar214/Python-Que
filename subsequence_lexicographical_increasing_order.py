s = input()
n = len(s)
subs = []

for i in range(1 << n):
    sub = ""
    for j in range(n):
        if i & (1 << j):
            sub += s[j]
    if sub:
        subs.append(sub)

subs.sort()
for sub in subs:
    print(sub, end=" ")


