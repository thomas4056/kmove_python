import random


for a in range(0,5):
    b=[0,0,0,0,0,0]
    for c in range(0,6):
        d=0
        while (d in b):
            d=random.randint(1,45)
        b[c]=d
    print("로또:"+ str(sorted(b)))

#sorted() 내장함수 이용: 문자열을 받아서 정렬시켜준다.
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

#b=[]
#d=0
#while d<5:
#    d=d+1
#    a=(random.randint(1,45))
#    b.append(a)
#    if len(b)==6:
#       print('로또%d='%(d),b)
