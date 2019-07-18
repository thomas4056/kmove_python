
import random,time

w=['cat','dog','fox','monkey','mouse','panda','frog','snake','wolf']
rank={}
def sortV(x):
    return x[1]                     #인덱스 (k,v)중 v값을 리턴

while True:
    print("1.문제불러오기 2.타자게임 3.등수목록 4.저장하기 5.불러오기")
    menu = input("메뉴를 선택하세요\n")
    if menu=='1':
        f=open("word.txt",'r')
        line=1
        #w.clear()  #지우고 싶으면 하면됨 아니면 주석
        while line:
            line=f.readline().replace("\n","")
            if not(line==''):
                w.append(line)
        print(w)
    elif menu=='2':
        n=1
        print("준비되면 엔터")
        input()
        start=time.time()
        q=random.choice(w)
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
        et=end-start
        et=format(et,".2f")
        print("타자 시간 :",et,"초")
        name= input("사용자 이름을 입력하세요")
        rank[name]=float(et)
    elif menu=='3':
        ranklist=sorted(rank.items(),key=sortV)
        #print(type(ranklist))      #ranklist의 타입을 알려면 사용
        num=1
        for k,v in ranklist:
            print("%d등 %s %f"%(num,k,v))
            num+=num
    elif menu=='4':
        f=open('rank.txt','w')
        text=''
        items=rank.items()
        for k,v in items:
            text=text+k+':'+str(v)+'\n'
        f.writelines(text)
        f.close()
    elif menu=='5':
        f=open('rank.txt','r')
        line=1
        while line:
            line=f.readline().replace("\n","")
        if not(line==''):
            k,v=line.split(':')
            rank[k]=float(v)
    else:
        print("잘못눌렀어요 ㅠㅠ\n다시 눌러 주세요")
