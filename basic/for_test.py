#for문 ---------------------->

#for i in range(2,10):
 #   for j in range(1,10):
  #      print(i*j , end=",")
   # print(" ")

#for a in range(1,10):
 #   for b in range(2,10):
  #      print(a*b , end="," )
   # print(" ")

for i in range(2,10):
    for j in range(1,10):
        print("%d*%d=%d" %(i,j,i*j),end="  ")
    print(" ")

for a in range(1,10):
    for b in range(2,10):
        print("%d*%d=%d" %(a,b,a*b),end="  ")
    print(" ")  #print()와 같음