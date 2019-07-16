a=[]
b=[1,2,3]
c=['life','is']
d=[1,2,'life']
e=[1,2,[1,2,3]]
#f=[1,2,3,[1,2,['life',2]]]

print(a)
print(b)
print(c)
print(d)
#print(e[3]) ----> #은 주석으로 사용이 가능하다.
print(e[2][1])

print(type(a))
print(e[-1][0]) #뒤의 괄호에서 앞에서 처음꺼 출력
#print(f[2][2][0]) # 뒤의 뒤 괄호안에서 처음꺼 ??? 알아보기

ab=[1,2,3] #바꾸기
ab[2]=4
print(ab)

del ab[1]   #지우기
print(ab)

ab.append([5,6])    #추가하기
print(ab)

ac=[5,3,6,1,4,8,9,]     #리스트 정렬 
ac.sort()               #아무것도 안적으면 오름차순 괄호에 reverse=Ture 적으면 내림차순
print(ac)

ac.sort(reverse=True)        #내림차순 ac.reverse() 사용해도 됨
print(ac)

#ba=[1,2,4,5,6,3]           #????
#ac.index(3)             #위치 값을 알려준다
#print(ba)              #알아보기

ac.insert(0,7)      #첫번째 자리에 4를 삽입
print(ac)

ac.remove(9)        #9를 제거
print(ac)

ad=[1,2,3,2,2]          #리스트의 맨 마지막 요소를 돌려주고 그 요소를 삭제한다.
ad.pop()
print(ad)

#ae=[1,2,3,2,2]      #???
#ae.count(2)         #리스트 안에 2가 몇개인지 알려줌
#print(ae)           #알아보기

af=[1,2,3]
af.extend([4,5])    #리스트에 4,5 추가하는 것
print(af)

#튜플 시작 ---> 리스트와 비슷 일단 괄호가 다르다 또 괄호안에 값을 바꾸지 못한다 요소가 한대여도 (1,) 뒤에 꼼마를 찍어야 함
#튜플을 제거나 변경을 하려하면 오류가 발생 하지만 인덱싱, 슬라이싱, 더하기, 곱하기는 가능

#딕셔너리 ---> 순서 무관한 경우 key:valus (key를 통해 접근)
#key는 중복 x 튜플이나 리스트는 순서가 있다. 
#생긴 모양은 {key:value} ex) dic={'name':'pey',phone:'01024084056'}

dic={1:10,2:{30,50},'name':'park'}     #꼭 문자일 필요는 x
print(dic)

ca={1:"a"}      #없는 2는 자동 생성
ca[2]="b"
print(ca)

#keys 는 key값만 뽑아내는 것 value는 value의 값는 뽑아내는 것
#item은 모두 뽑아내는 것
print(dic.keys())
print(dic.values())
print(dic.items())
#clear은 지우기 get은 얻기 키안에 값을 출력 in은 있는지 없는지 알려줌
cb={4:5,6:7}
print(cb.clear())
print(dic.get(1))
print('name' in dic)

#Ture 참 False 앞에는 대문자 적어줘야함 

#if문 시작 --->
  