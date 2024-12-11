x = int(input())
arr =list(map(int,input().split()))

five = 0
ten=0
twenty = 0

for i in arr:
    if i==5:
        five += 1
    elif i==10:
        if five<2:
            print("false") 
            exit()
        else:
            ten+=1
            five -=1
    
    elif i==20:
        if five<3 and ten==0:
            print("false")
            exit()
        
        else:
            twenty +=1
            five -=1
            ten-=1        
                   
print("True")                   