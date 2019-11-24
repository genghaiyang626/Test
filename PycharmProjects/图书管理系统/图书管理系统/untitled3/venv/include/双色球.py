import random
redball=[]
blueball=0
for i in range(1,7):
    redball.append(random.randint(1,33))
blueball=random.randint(1,16)
n=len(redball)
for i in range(n):
   for j in range(0,n-i-1):
       if redball[j]>redball[j+1]:
           redball[j], redball[j + 1] = redball[j + 1], redball[j]
print("本期的双色球号码为：",redball,blueball)