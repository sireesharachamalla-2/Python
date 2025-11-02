
class Meeting:
    def __init__(self,title,content):
        self.title=title
        self.content=content
    def display(self):
        print(self.content)
class List(Meeting):
    def __init__(self,title,items):
        content=", ".join(items)
        super().__init__(title,content)
        self.items=items
    def disply(self):
        for i in (self.items,1):
            print(i)
m_obj=Meeting("Meeting Notes","Discuss project status with team.")
g_obj=List("grocery List",["eggs","milk","bread"])
m_obj.display()
g_obj.display()
