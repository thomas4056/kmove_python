#타자게임    random.choice()사용 

#for i in range(0,5):
#    while dd=5:
#======================
#c=str(print(b))
#d=str(input("단어를 적으시오\n"))
#if c==d:
#    print("정답입니다")
#else:
#    print("다시 입력해 주세요")
import random
import time
n=1
w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
q=random.choice(w)
input("시작")
start=time.time()
while n<=5:
    print("문제",n)
    print(q)
    x=input()
    if q==x:
        print("통과")
        n=n+1
        q=random.choice(w)
    else:
        print("오타! 다시도전!")
        
end=time.time()
t=end-start
print("타자 시간:{:.0f}초".format(t))