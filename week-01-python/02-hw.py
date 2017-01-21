#사람 클래스
class People:

    def __init__(self,name,age,gender,position):
        self.name=name
        self.age=age
        self.gender=gender
        self.position=position

#### Article class inheritance 상속
class colleague(People):
    position="대리"

name=input("이름을 입력해주세요")
age=input("나이를 입력해주세요")
gender=input("성별을 알려주세요")
position=input("직급을 알려주세요")

a=People(name,age,gender,position)
print(a.__dict__)
