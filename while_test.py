listdata=[]
while True:
    print('''
    ====================리스트 관리=====================
    1. 리스트에 추가 2.리스트 데이터 수정 3. 데이터 삭제 4. 종료
    ''')
    menu=int(input("메뉴를 선택하세요\n"))

    if menu == 4:   # 설명 break 가장 근접한 반복문 벗어남
        break
    elif menu == 1:
        data=input("추가할 데이터를 입력하세요\n")
        listdata.append(data)
        print(listdata)
    elif menu ==2:
        #data1= input("수정하고싶은 데이터를 입력하세요\n")
        #data2= input("수정할 데이터를 입력하세요\n")
        #listdata[data1]=data2
        #listdata.remove(data1)
        #listdata.append(data2)
        #data4=int(input("수정하고싶은 데이터를 입력하세요\n"))
        #data5=int(input("수정할 데이터를 입력하세요\n"))
        #data6=data4+1
        #listdata[data6]=data5
        num=int(input("입력하세요\n"))
        data7=input("변경할 것을")
        
        print(listdata)
    elif menu ==3:
        data3= input("삭제할 데이터를 입력하세요\n")
        listdata.remove(data3)
        print(listdata)
    else:
        print("잘 못 적었습니다\n다시적어주세요")
