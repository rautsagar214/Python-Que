answerKey = input().strip()
k = int(input())

if not answerKey:
    print(0)
else:
    max_length = 0
    for char in ["T", "F"]:
        left = 0
        num_changes = 0

        for i in range(len(answerKey)):
            if answerKey[i] != char:
                num_changes += 1 

            while num_changes > k:
                if answerKey[left] !=   char:
                    num_changes -= 1
                left += 1

            max_length = max(max_length, i - left + 1)

    print(max_length)
    