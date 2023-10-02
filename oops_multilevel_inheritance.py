class Parent:
    def parent_name(self,parentname):
        self.parentname=parentname
    def show_parentname(self):
        print("Parent name is late. Ram Naresh Mishra")
class Child(Parent):
    def child_name(self,childname):
        self.childname=childname
    def show_childname(self):
        print("Child name is Mr. Amarnath Mishra")
class GrandChild(Child):
    def grand_child_name(self,grandchildname):
        self.grandchildname=grandchildname
    def show_grandchildname(self):
        print("grandChild name is Ankita Mishra")
        print("grandChild name is Anshuman Mishra")
        print("grandChild name is Abhijeet Mishra")
        print("grandChild name is Himanshu Mishra")
c1=GrandChild()
c1.show_parentname()
c1.show_childname()
c1.show_grandchildname()
