#time.time() 이용
import time
input("엔터를 누르고 20초를 세고 다시 엔터를 눌러주세요\n")
a=time.time()
input("20초면 엔터 ㄱㄱ")
b=time.time()
c=b-a
d=20-c
print("실제시간:%s\n차이시간:%s"%(d,c))
    #abs 절대값


#=========================================
import random

a=(random.sample(range(1,10),3))
print(a)

b=input("원하는 숫자를 입력하세요")
bb=input("원하는 숫자를 입력하세요")
bbb=input("원하는 숫자를 입력하세요")
c=a.index(b)
cc=a.index(bb)
ccc=a.index(bbb)
print(c)

if c==0 or cc==1 or ccc==2:
    print("1스트라이크")
elif c==0 and cc==1 or c==0 and ccc==2 or cc=1 and ccc=2:
    print("2스트라이크")
elif c==0 and cc==1 and ccc==2:
    print("3스트라이크")