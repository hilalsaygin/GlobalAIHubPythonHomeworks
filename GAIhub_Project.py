import random
class Student():
    def __init__(self, name,surnm):
        self.name=name
        self.surnm=surnm
        self.courses={} # key=course name:value= objects of Courses class. lenght must be min 3 max 5
    def welcoming(self):
        print("WELCOME to the class {} {} ".format(self.name,self.surnm))

class Courses():
    def __init__(self, c_nm): #grades={mt:mtgrades,final:fgrade:project:pgrade}
        self.course_nm = c_nm
        self.grades = {}
        self.letter_grade=''

    def generate_grades(self):
        self.grades={'Midterm':random.randint(0,100), 'Final': random.randint(0,100),'Project':random.randint(0,100)}

    def total_grade(self):
        gr_list=list(self.grades.values())
        tot_grade=gr_list[0]*0.3 + gr_list[1]*0.5 + gr_list[2]*0.2
        return tot_grade


def Create_Student():
    wrong_info = 0
    file_lines = [l.strip('\n').upper().split('\t') for l in open('studentlist.txt', 'r').readlines()]

    while wrong_info < 3:
        nm = input("Please, Enter your Name  ").upper()
        srnm = input("Please, Enter your Surname  ").upper()
        for line in file_lines:
            if line[0] == nm and line[1]==srnm:
                std = Student(nm, srnm)
                std.welcoming()
                return std
        print("Your name and surname are not registered in the system!! Please try again!! ")
        wrong_info += 1
    print("You entered name and surname incorrectly 3 times !! Please Try Again Later !!")
    exit()

def StudentManagementSystem():      #fills the courses list for each student. given parameter course is objects of Courses class
    student = Create_Student()
    created_courses = list()
    c_count=1
    while c_count<6:
        cr=input("Please, Enter Course {} to create :".format(c_count))
        if cr not in created_courses and cr != "":
            created_courses.append(cr)
            c_count += 1
        elif cr in created_courses:
            print("Course {} already created !!".format(cr.upper()))
        else:
            "You must enter a valid course name !!"

    course_num=5
    print("Enter the course name that You'd like to take. >> If You do not want to take any course press 0 \nThe courses You can take : ")
    for c in range(len(created_courses)):
        print(c+1,'-'+ created_courses[c])
    while 0 < course_num <=5:
        take_crs = input("Choose a Course to take :")
        try:
            if int(take_crs) == 0:
                break
        except ValueError:
            if take_crs in created_courses and take_crs not in student.courses.keys():
                student.courses[take_crs]=Courses(take_crs)
                course_num-=1
            elif take_crs not in created_courses:
                print("Course --{}-- has not created!! You cannot take a course that hasn't created .".format(take_crs.upper()))
            elif take_crs in student.courses.keys():
                print("You already took course --{}-- ".format(take_crs.upper()))

    if len(student.courses.keys())<3:
        return "You failed in class!! You cannot take less than 3 course to pass in this class!!"

    elif 3 <= len(student.courses) <= 5:
        exam_list=[]
        while input("\nDo you want to take an Exam,Yes/No ? ").lower() != 'no':
            print("Your course list : >> {} " .format('  >> '.join(student.courses.keys())))
            ex_crs = input("Exam Time!! :D  Choose a course from your list to take the exams:")
            if ex_crs in student.courses and ex_crs not in exam_list:
                for c_nm, course_obj in student.courses.items():
                    if c_nm ==ex_crs:
                        course_obj.generate_grades()
                        total=course_obj.total_grade()
                        exam_list.append(ex_crs)
                        if total > 90:
                            course_obj.letter_grade = 'AA'
                        elif total >= 70:
                            course_obj.letter_grade = 'BB'
                        elif total >= 50:
                            course_obj.letter_grade = 'CC'
                        elif total >= 30:
                            course_obj.letter_grade = 'DD'
                        elif total < 30:
                            course_obj.letter_grade = 'FF'

                for course_obj in student.courses.values():
                    if course_obj.course_nm ==ex_crs:
                        print("Your grades for course --{}-- \n ".format(course_obj.course_nm.upper()))
                        for ex, grade in course_obj.grades.items():
                            print(ex, grade)
                        print('Letter Grade :' ,course_obj.letter_grade)
                        if course_obj.letter_grade =='FF':
                            print("Failed in --{}-- !! \n".format(course_obj.course_nm.upper()))
                        else:
                            print("Passed in --{}-- \n".format(course_obj.course_nm.upper()))
            elif ex_crs in exam_list:
                print("You already took the exam for --{}--\n".format(ex_crs.upper()))
            else:
                print("Course --{}-- is not in your courses. You cannot take its exam!! \n".format(ex_crs.upper()))

message=StudentManagementSystem()
if message != None:
    print(message)




