class Father:
    def father_name(self,fathername):
        self.fathername=fathername
    def show_fathername(self):
        print("father name is Mr.Amar nath Mishra")
class Mother:
    def mother_name(self,mothername):
        self.mothername=mothername
    def show_mothername(self):
        print("mother name is Mrs. Pramila Devi")
class Child(Father,Mother):
    def child_name(self,childname):
        self.childname=childname
    def show_childname(self):
        print("Child name is Ankita Mishra")
        print("Child name is Anshuman Mishra")
        print("Child name is Abhijeet Mishra")
        print("Child name is Himanshu Mishra")
c1=Child()
c1.show_fathername()
c1.show_mothername()
c1.show_childname()
