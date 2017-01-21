#class 복습

class School:
    name="University"
    yr="1950"
    address="Dublin 308"

    def __init__(self,name,yr,address):
        self.name=name
        self.yr=yr
        self.address=address

print(School.name)
print(School.yr)
print(School.address)
