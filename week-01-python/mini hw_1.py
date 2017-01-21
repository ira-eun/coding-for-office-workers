#list 나 tuple 에서 임의의 하나 값을 뽑으려면
L=list(range(1,6))
print(L)
import random
print(random.sample(L,1))

T=tuple
T=[1,2,3,4,5]
print(T)
print(random.sample(T,1))
