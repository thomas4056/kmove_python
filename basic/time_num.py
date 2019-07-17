import random   #import random,time 해도됨
import time

count=0
oper=['+','-','*','/']
input("엔터를 누르면 시작\n")
aa=time.time()    

for x in range(0,5):
    a=random.randint(1,50)
    b=random.randint(1,50)
    op=random.choice(oper)

    quiz= str(a)+op+str(b)
    quiz='%d %s %d'%(a,op,b)

    print(quiz,'=')
    print(eval(quiz))
    c=int(input("정답="))

    if int(eval(quiz))==c:
        print("정답!")
        count+=1
    else:
        print("오답!")

bb=time.time()
cc=bb-aa
print("%d개 맞음"%count)
print("걸린 시간은%.0f초입니다"%cc)       #%.0f로 사용이 가능함 소수점 없는거