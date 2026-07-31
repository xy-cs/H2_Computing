from flask import*

#Task 4.1
import sqlite3

connection = sqlite3.connect("school.db")
connection.execute("DROP TABLE IF EXISTS People")
connection.execute("CREATE TABLE 'People' ("+
                   "'PersonID'	INTEGER PRIMARY KEY AUTOINCREMENT,"+
                   "'FullName'	TEXT NOT NULL,"+
                   "'DateOfBirth'	TEXT NOT NULL,"+
                   "'ScreenName'	TEXT NOT NULL,"+
                   "'IsAdult'	INTEGER NOT NULL)"
                   );
connection.close()

#Task 4.2
import sqlite3
from datetime import date
class Person:
    def __init__(self, full_name, date_of_birth):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
    
    def name(self):
        return self.full_name
    
    def setname(self, name):
        self.full_name = name
        return self.full_name
    
    def dateOfBirth(self):
        return self.date_of_birth
    
    def setdata(self, date):
        self.date_of_birth = date
        return self.date_of_birth
    
    def is_adult(self):
        year = int(self.date_of_birth[:4])
        yearnow = date.today().year
        age = yearnow - year
        if age >= 18:
            return True
        else:
            return False
    
    def screen_name(self):
        name = self.full_name
        screenname = ""
        for i in name:
            if i.isalpha():
                screenname += i
        for a in self.date_of_birth[4:]:
            if a.isdigit():
                screenname += a
        return screenname

#part 2
class Staff(Person):
    def __init__(self, full_name, date_of_birth):
        super().__init__(full_name, date_of_birth)
    
    def is_adult(self):
        return True
    
    def screen_name(self):
        name = super().screen_name()
        return name + "Staff"

class Student(Person):
    def __init__(self, full_name, date_of_birth):
        super().__init__(full_name, date_of_birth)
    
    def is_adult(self):
        return False


#part 3
connection = sqlite3.connect("school.db")

with open("people.txt",'r') as file:
    file = file.readlines()
    #file closes automatically

for i in range(len(file)):
    adultnum = 2
    file[i] = file[i].strip('\n').split(',')
    if file[i][2] == "Person":
        person = Person(file[i][0], file[i][1]) #run person class
        adult = person.is_adult()
        screenname = person.screen_name()
    elif file[i][2] == "Staff":
        person = Staff(file[i][0], file[i][1]) #run staff class
        adult = person.is_adult()
        screenname = person.screen_name()
    elif file[i][2] == "Student":
        person = Student(file[i][0], file[i][1]) #run student class
        adult = person.is_adult()
        screenname = person.screen_name()
    else:
        print("Data is invalid")
    if adult == True :
        adultnum = 1
    else:
        adultnum = 0
    connection.execute("INSERT INTO People(FullName, DateOfBirth, ScreenName, IsAdult) VALUES"+
                       "(?, ?, ?, ?)", (file[i][0], file[i][1], screenname, adultnum,))
    connection.commit()
        
connection.close()
#main
person = Person("John Tan", "2000-06-01")
print(person.is_adult())
print(person.screen_name())

staff = Staff("John Tan", "2000-06-01") # staff
print(staff.is_adult())
print(staff.screen_name())

student = Student("Merry Tan", "2018-06-01") # student
print(student.is_adult())
print(student.screen_name())

#Task 4.3
app = Flask(__name__)

@app.route('/')
def index():
    with open("people.txt",'r') as file:
        file = file.readlines()
        #file closes automatically
    print(file)
    records = []
    for i in file:
        i = i.split(',')
        i[2] = i[2].strip('\n')
        screenname = ""
        if i[2] == "Person":
            person = Person(i[0], i[1]) #run person class
            screenname = person.screen_name()
        elif i[2] == "Staff":
            person = Staff(i[0], i[1]) #run staff class
            screenname = person.screen_name()
        elif i[2] == "Student":
            person = Student(i[0], i[1]) #run student class
            screenname = person.screen_name()
        i[1] = screenname
        records.append(i)
    print(records)
    ##for i in rows:
        
    return render_template("Task4_3_xy_25S11.html", records = records)
    

##screen_names = []
###for row in rows:
## #   screen_names.append(row)
##with open("people.txt",'r') as file:
##    file = file.readlines()
##    #file closes automatically
##print(file)
##records = []
##for i in file:
##    records.append(i.strip())
##print(records)
if __name__ == '__main__':
    app.run(debug = True, port = 1234)
print(index())
