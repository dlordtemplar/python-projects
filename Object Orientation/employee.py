'''
Exercise (4 points)

a) Write a class that represents a course. The class should represent the
   following information:

- title

- day

- start time

- end time

  (Assume for simplicity that meetings for courses take place just once a week)


b) Write a class that represents employees of a university.

The class should contain attributes representing the following information:

- Employees have a first name, a last name and a birth date

- Employees might be teaching one or more courses (represented as strings).
  Initially, i.e., when an Employee object is created, no courses should
  be assigned to the employee.

Plus at least the following methods:

- add_course: assign a course to the employee

- is_avalailble: returns True if the Employee is available for a meeting.
  Assume that the employee is available at all times where they do not 
  give a course.

- a __str__ method the returns a string where all information is nicely 
  presented 
'''


class Course:
    def __init__(self, title, day, startTime, endTime):
        self.title = title
        self.day = day
        self.startTime = startTime
        self.endTime = endTime

    def __str__(self):
        return "Title: " + self.title + "\tDay: " + self.day + "\tStart time: " + self.startTime + "\tEnd Time: " + self.endTime


class Employee:
    def __init__(self, fName, lName, bDate):
        self.fName = fName
        self.lName = lName
        self.bDate = bDate
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def is_available(self, day, time):
        free = True
        for course in self.courses:
            if free:
                if day == course.day:
                    if course.endTime >= time >= course.startTime:
                        free = False
        return free

    def __str__(self):
        courseList = ""
        for course in self.courses:
            if courseList != "":
                courseList += ", "
            courseList += course.title
        if courseList == "":
            courseList = "no courses"
        return self.fName + " " + self.lName + ", born " + self.bDate + " teaches " + courseList

if __name__ == "__main__":
    print("Create employee 'John Doe', born January 1st, 1990")
    john = Employee('John', 'Doe', '1990-01-01')
    print('  Created:', john)
    
    print("Create employee 'Jane Doe', born August 10, 1992")
    jane = Employee('Jane', 'Doe', '1992-08-10')
    print('  Created:', jane)
    
    print("Add 'Python I' to John Doe's courses")
    python1 = Course('Python I', 'Tuesday', 12, 14)
    john.add_course(python1)
    print('  John:', john)
    
    print("Add 'Introduction to Semantics' to John Doe's courses")
    semantics = Course('Introduction to Semantics', 'Monday', 10, 12)
    john.add_course(semantics)
    print('  John:', john)
    
    print("Add 'Python I' to Jane Doe's courses")
    jane.add_course(python1)
    print('  Jane:', jane)
    
    print("Is John avaliable for a meeting on Monday at 11h?")
    print(john.is_available('Monday', 11))

    print("Is Jane avaliable for a meeting on Monday at 11h?")
    print(jane.is_available('Monday', 11))

    print("Is John avaliable for a meeting on Tuesday at 13h?")
    print(john.is_available('Tuesday', 13))
    
    print("Is John avaliable for a meeting on Tuesday at 15h?")
    print(john.is_available('Tuesday', 15))
    
