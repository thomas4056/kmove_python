#import math   제곱근=math.sqrt
'''
def add(a,b):
    return a+b

print(add(5,4)) #a,b는 매개변수
c=add(5,6)      #5,6은 인수
print(c)

def add_many(choice,*a):
    result=0
    print(type(a))
    print(a)
    for i in a:
        result=result+i
    return result

total = add_many(1,2,3,4,5,6,7,8,9,10)
print(total)
'''
'''
def add_add_mul(a,b):
    return a+b,a*b



#total=add_add_mul(3,6)
#print(type(total))
#print(total)

add,mul=add_add_mul(3,6)
print(type(add))
print(type(mul))
print(add)
print(mul)

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다."%name)
    print("나이는 %d살입니다."%old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself("문태일",25,True)
say_myself("김민주",23,False)
'''

a=1
alist=[1,2,3]
#list and 딕션어리는 한수 안에서도 영향을 받음 하지만 a(int)는 영향을 받지 않음
def add_data(a):
    a=a+1
    alist.append(4)
    print("안쪽 %d"%a)
add_data(a)
print("바깥쪽 %d"%a)
print(type(a))
print(type(alist))