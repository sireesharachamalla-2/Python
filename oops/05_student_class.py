class Student:
    school_name="AVN High School"
    def __init__(self,name):
        self.name=name
        
    
s1=Student("sneha")
s2=Student("sireesha")
print(s1.school_name)
print(s2.school_name)