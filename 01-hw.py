# 메뉴정하기

menu=input("한식, 중식, 일식 중 하나를 선택해주세요.")
L=list
L=["경복궁","털보네","청목","남원집"]
if menu=="한식":
    import random
    print(random.sample(L,1))

L2=list
L2=["하오커","루이","중화반점","이연복"]
if menu=="중식":
    import random
    print(random.sample(L2,1))

L3=list
L3=["스시조","모모야마","모리타","이키오쿠"]
if menu=="일식":
    import random
    print(random.sample(L3,1))
