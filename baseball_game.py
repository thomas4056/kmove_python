#random.samle()이용 야구게임
import random

#a=(random.sample(range(1,10),3))
#print(a)

#b=int(input("첫번째 숫자를 입력하세요"))
#bb=int(input("두번째 숫자를 입력하세요"))
#bbb=int(input("세번째 숫자를 입력하세요"))
#c=a.index(b)
#cc=a.index(bb)
#ccc=a.index(bbb)

#if c==0 or cc==1 or ccc==2:
#    print("1스트라이크")
#elif c==0 and cc==1 or c==0 and ccc==2 or cc=1 and ccc=2:
#    print("2스트라이크")
#elif c==0 and cc==1 and ccc==2:
#    print("3스트라이크")\
#=========================================================
com=random.sample(range(1,10),3)
print(com)
strike=0
check=0
print("시작")
while strike !=3:
    strike=0
    ball=0
    guess=list(input("3자리 숫자를 입력하세요"))
    print(guess)
    for a in guess:
        for b in com:
            if int(a)==b:
                if guess.index(a)==com.index(b):
                    strike+=1
                else:
                    ball+=1
    check+=1
    print("스트라이크:%d, 볼:%d, 시도횟수%d"%(strike,ball,check))
print("정답")