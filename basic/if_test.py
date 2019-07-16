#money= True
#if money:
#    print("택시를 타고 가라")   #pass는 공백을 만드는 것이다
#else:
#    pass           #----------------------------까지 if문이다
#print("걸어가라")   #중첩이 만으면 고치기 어려움 최대한 중첩 x (if 1번만 사용이 좋음)

#mon= True           #탭 맞춰야지 오류가 안남
#if mon:
#    print("택시를 타고 가라") 
#else:         
#    print("걸어가라")
#elif 다른 조건  처음에 if 중간 elif 마지막 else

#jum =input("성적을 입력하세요\n") #int 정수 str---???
#print(jum)

#j=int(input("성적을 입력하세요\n"))     #나의 솔루션
#if 90<=j<=100:
#    print("당신의 학점은 A입니다.")
#elif 80<=j<90:
#    print("당신의 학점은 B입니다.")
#elif 70<=j<80:
#    print("당신의 학점은 C입니다.")
#elif 60<=j<70:
#    print("당신의 학점은 D입니다.")
#else:
#    print("당신의 학점은 F입니다.")
#-------------------------------------------교수님 솔루션+설명
ju=int(input("성적을 입력하세요\n"))
print("입력힌 성적은 %d 입니다"%ju)
#print("입력한 성적은 ",ju,"입니다") 이것도 가능
if ju>=90:
    total='A'
elif ju>=80:
    total='B'
elif ju>=70:
    total='C'
elif ju>=60:
    total='D'
else:
    total='F'
print("당신의 성적은 {} 입니다.".format(total))
