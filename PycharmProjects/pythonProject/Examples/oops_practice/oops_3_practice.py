# class Person():
#     def __init__(self,name,age,location):
#         self.name=name
#         self.age=age
#         self.location=location
#
# info=Person("Avinash",27,"nellore")
# print(info.name,info.age,info.location)


# class Person():
#     def __init__(self,name,age,location):
#         self.name=name
#         self.age=age
#         self.location=location
#         print(f"name:{name},age:{age},location:{location}")
#
# info=Person("avinash",27,"nellore")



class Hospital():
    def __init__(self,hospital_name,city,doctor):
        self.hospital_name=hospital_name
        self.city=city
        self.doctor=doctor
        print(f"hospital_name:{self.hospital_name},city:{self.city},doctor:{self.doctor}")

hospital_info=Hospital("kims","hyd","reddy")




