# 1) 사용자로 부터 몇단을 출력할 지 받을 것
# 2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것

dan=int(input("몇단을 출력하시겠습니까?"))
for num in range(1,10):
    print("{}*{}={}".format(dan,num,dan*num))
