#사칙연산 숫자 2개와 연산자 임의 추출
#eval() 알아보기 random.choice()

import random

#for i in (0,5):
a=random.randint(1,10)
b=random.randint(1,10)
e=('+','-','*','/')
c=random.choice(e)
f=print(str(a)+c+str(b))
print(eval(str(a)+c+str(b)))
g=eval(str(a)+c+str(b))
h=int(input("답을 적어주세요\n"))
if h==g:
    print("정답입니다")
else:
    print("틀렸습니다.")
num=0
num=num+1

#print(eval('2+3'))
#===============================교수님꺼 아래========================
#count=0
#oper=['+','-','*','/']
#for x in range(0,5):
#    a=random.randint(1,50)
#    b=random.randint(1,50)
#   op=random.choice(oper)

#    quiz= str(a)+op+str(b)
#    quiz='%d %s %d'%(a,op,b)

#    print(quiz,'=')
#    print(eval(quiz))
#    c=int(input("정답="))

#    if int(eval(quiz))==c:
#        print("정답!")
#        count+=1
#    else:
#        print("오답!")
#print("%d개 맞음"%count)
