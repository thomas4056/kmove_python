import pickle       #pickle은 외부에 있는 라이브러리 사용

data={1:'python',2:'you'}

f=open('test_p.txt','wb')
pickle.dump(data,f)        #dump와dumps가 있다. 거의 맞춰놓음
f.close()

f=open('test_p.txt','rb')
data1=pickle.load(f)
f.close()

print(data)
print(data1)
print(type(data1))

#pneumonoultramicroscopicsilicovolcanoconiosis
#누모노 울트라 마이크로 스코픽 실리코 볼커노(볼케이노 아닙니다) 커니어시스
