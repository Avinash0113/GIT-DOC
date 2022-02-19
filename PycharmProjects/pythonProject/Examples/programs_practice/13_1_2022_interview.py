class Parent_1():
    def property(self):
        print("Parent_1 : having house")

    def sport(self):
        print("Parent_1 : play's valleyball")

class Parent_2():
    def sport(self):
        print("parent_2 : play's cricket")
    def scooty(self):
        print("parent_2: drives scooty")


class Parent_3():
    def sport(self):
        print("parent_3 : play's baseball")
    def scooty(self):
        print("parent_3: drives scooty")


class Child(Parent_3,Parent_1,Parent_2):
    def Bike(self):
        print("iam having a bike")
    def Mobile(self):
        print("iam having mobile")

obj_1 = Child()

obj_1.sport()







