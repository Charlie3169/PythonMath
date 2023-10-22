sum = 0
for i in range (1,1001):
    if(i % 4 == 0 or i % 6 == 0 or i % 9 == 0):        
        sum += 1

print(sum)

sum2 = 0
for i in range (1,1001):
    if(i % 4 != 0 and i % 6 != 0 and i % 9 != 0):        
        sum2 += 1

print(sum2)
