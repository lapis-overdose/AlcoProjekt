from datetime import datetime



class TaskManager:

    def __init__(self,name,start,end,status):
        # atributes
        self.name = name
        self.start = datetime.strptime(start, "%d,%m,%Y")
        self.end = datetime.strptime(end, "%d,%m,%Y")
        self.status = status

        #УДАЛИТЕ pass КОГДА БУДЕТЕ ДЕЛАТЬ

    def displayTasks(self): #менюшка
        pass

    def settings(self):
        pass

    def addTask(self):
        pass

    def deleteTask(self):
        pass


