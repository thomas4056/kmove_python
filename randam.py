#import random

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
#====================================================================================================
#for a in range(0,5):
#    b=[0,0,0,0,0,0]
#    for c in range(0,6):
#        d=0
#        while (d in b):
#            d=random.randint(1,45)
#        b[c]=d
#    print("로또:"+str(sorted(b)))
#====================================================================================================
#import random                #외부함수
#for a in range(0,5):           #0부터4까지 돌림 (5번만돌리면 됨 0이든1이든 노상관)
#    b=[0,0,0,0,0,0]
#    for c in range(0,6):        #6개를 뽑는 것 (0부터 5까지)
#        d=0                     #초기값 0
#        while (d in b):         #1부터45사이의 숫자 뽑음 (번호 중복 x,반복)
#            d=random.randint(1,45)
#        b[c]=d
#    print("로또:",sorted(b))

#import random               #위에 예제와 같은 결과 값이 나옴
#for i in range(1,6):
#    print("로또 :" ,sorted(random.sample(range(1,46),6)))

#사칙연산 숫자 2개와 연산자 임의 추출

a=[1,2,3,4]
input("숫자")
b=a.index()
print(b)