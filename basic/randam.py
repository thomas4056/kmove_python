import random

#sorted() 내장함수 이용: 믄자열을 받아서 정렬시켜준다.
#b=[]
#while True:
    #a=(random.randint(1,45))
    #b.append(a)
    #d=0
    #d=d+1
    #if len(b)==6:
     #   print('로또%d='%(d),b)
      #  b.remove(a)
    #elif d>6:
     #   break

b=[]
a=(random.randint(1,45))
b.append(a)
while True:

    for d in range(1,6):
        if d<6:
            break
            print('로또%d='%(d),b)
