print('hi')
print("hi")
food="python's favorite\n \"food\" is perl"
print(food)
print('123','한글','영어',sep='-',end='')
print('다음줄임')
head="python"
tail="is fun"
number1=1
number2=2

print(head+tail)
print(head*3)
print(number1+number2)
print("="*50)
print(len(food))
print(food[-1])
print(food[0:8])
print(food[:8])
print(food[8:])

b=10.1111221
print("i eat %d apples." %b)
day='there'
c='i ate %d apples. so i was sick for %s days.'%(b,  day)
print(c)

print('i eat %.2f apples.'%b)
print('i eat %.5f apples.'%b)
print('i eat %20d apples.'%b)

print("python's {}favorite food is perl".format(b))
print("python's {1}favorite{0} food is perl".format(b,20))


print("i like {p} but i don't like {d}" format(p='3',d='20'))