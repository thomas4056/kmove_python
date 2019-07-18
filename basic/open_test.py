'''
#파일 생성 open 사용 (encodimg="utf8")
f=open("basic/test.txt","w", encoding="utf8")

for i in range(1,11):
    data='%d번째 줄입니다.\n'%i
    f.write(data)

f.close()
#readline 한줄씩 읽는 것
#readlines 한꺼번에 읽는다 list로 표현
#read 한꺼번에 읽는 것 (줄바꿈 문자)
'''
'''
f=open("basic/test.txt","r",encoding="utf8")
line=f.readline().replace("\n",'')
print(line,end='')
print(type(line))
f.close()
'''
'''
f=open("basic/test.txt","r",encoding="utf8")
line=f.readlines()
print(line)
print(type(line))
for lines in line:
    print(lines.replace('\n','')) #replace 없으면 다름

f.close()
'''
'''
f=open("basic/test.txt","r",encoding="utf8")
line=f.read()
print(line)
print(type(line))
'''
#새로운 내용 추가하기
f=open("basic/test.txt","a",encoding="utf8")
for i in range(11,20):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
    
f.close()

#pickle 개체단위 저장 개체단위 받아옴 등등... 많음(편함)
#점프 투 파이썬에서 보기

