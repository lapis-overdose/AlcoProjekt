ИНСТРУКЦИЯ ПО ВЫЖИВАНИЮ  


// обновление 1
*В пизду сортировку
*Добавлен datetime
 ВАЖНО!!! НЕОБХОДИМО ВВЕСТИ В cmd - pip install datetime


//////////////////////////////////////////////
Пример программы

Select name of task
Holocost
Select day when task will start dd/mm/yr
01,01,1941


 Name       Start date   Due to      Priority
1 Holocost  01,01,1941   02,01,1941  Highest
2 smth      01,01,1111   03,03,1488  Low
_____________________________________________
*settings - to open settings

settings
 

  Name      Start date   Due to      Priority
1 Holocost  01,01,1941   02,01,1941  Highest
2 smth      01,01,1111   03,03,1488  Low
_____________________________________________
*add - to add task 
*delete - to delete task
*back - to back to the home
/////////////////////////////////////////////


    def displayTask(self): #менюшка
	pass

    def settings(self): #удаляется *settings *priority_up , заменяется на *add *delete *back
        pass

    def addTask(self):
        pass

    def deleteTask(self):
        pass

