import random
from tabulate import tabulate

list_of_courses = []
list_of_User = []

class User:
    def __init__(self, id, name, email, phone, address, list_of_courses, user_type, ):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.list_of_courses = list_of_courses
        
        self.user_type = user_type

    def __str__(self):
        return f"{self.user_type}: {self.name} (ID: {self.id})"

class Courses:
    def __init__(self, C_id, C_name, C_des, C_type):
        self.C_id = C_id
        self.C_name = C_name
        self.C_des = C_des
        self.C_type = C_type

    def __str__(self):
        return f"{self.C_name} (ID: {self.C_id})"

class Function:
    def __init__(self):
        pass

    def gen_id(self, user_type):
        temp_id = user_type + str(random.randint(1, 90000))
        if self.validate_user_id(user_type, temp_id):
            return temp_id
        return self.gen_id(user_type)

    def gen_cid(self):
        return "course" + str(random.randint(1, 90000))

    def validate_user_id(self, user_type, id):
        if user_type.lower() in ["staff", "student"]:
            return all(data.id != id for data in list_of_User)
        else:
            return all(data.C_id != id for data in list_of_courses)

    def adduser(self):
        try:
            type_user = int(input("1. Add student:\n2. Add staff:"))
            if type_user not in [1, 2]:
                print("Invalid selection. Please choose 1 or 2.")
                return
            
            users = {1: "Student", 2: "Staff"}
            user_obj = User(
                self.gen_id(users[type_user]),
                input("Name: "),
                input("Email: "),
                input("Phone: "),
                input("Address: "),
                [],  # Assuming an empty list for courses initially
                users[type_user],
                
            )
            
            list_of_User.append(user_obj)
            print("User  added....\n", f"Id: {user_obj.id}")

        except ValueError:
            print("Invalid input. Please enter a number.")

    def addcourse(self):
        course_obj = Courses(
            self.gen_cid(),
            input("Course Name: "),
            input("Description: "),
            input("Course Type: ")
        )
        
        list_of_courses.append(course_obj)
        print("Course Added....\n", f"Course Id: {course_obj.C_id}")

    def viewuser(self):
        tp = input("1. For student \n2. For staff: ")
        if tp == "1":
            user_data = [
                {
                    "User  Type": user.user_type,
                    "ID": user.id,
                    "Name": user.name,
                    "Email": user.email,
                    "Phone": user.phone,
                    "Address": user.address,
                    "Courses Studying": user.list_of_courses
                }
                for user in list_of_User if user.user_type == "Student"
            ]
            print(tabulate(user_data, headers="keys", tablefmt="pretty"))
         
        elif tp == "2": 
            user_data = [
                {
                    "User  Type": user.user_type,
                    "ID": user.id,
                    "Name": user.name,
                    "Email": user.email,
                    "Phone": user.phone,
                    "Address": user.address,
                    "Courses Teaching": user.list_of_courses
                }
                for user in list_of_User if user.user_type == "Staff"
            ]
            print(tabulate(user_data, headers="keys", tablefmt=" pretty"))
        else:
            print("Enter valid option")

    def viewcourse(self):
        course_data = [
            {
                "Course ID": course.C_id,
                "Course Name": course.C_name,
                "Description": course.C_des,
                "Course Type": course.C_type
            }
            for course in list_of_courses
        ]
        print(tabulate(course_data, headers="keys", tablefmt="pretty"))
    
    def searchuser(self,id):
        for u in list_of_User:
            if u.id==id:
                user_data=[{"user type":u.user_type,"ID":u.id, "name":u.name, "email":u.email, "add":u.address,"phone":u.phone}]
                print(tabulate(user_data, headers="keys", tablefmt=" pretty"))
       
    def assigncourse(self):
        ac=int(input("1.Assign course to student \n2.Assign course to staff")) 
        if ac==1:
            c=input("Enter course id:")
            for l in list_of_courses:
                if l.C_id==c:
                    print("Course name:",l.C_name)
            s=input("Enter student id:")
            for l in list_of_User:
                if l.id==s:
                    l.list_of_courses=c
                    print(l.name)
            
        elif ac==2:
                c=input("Enter course id:")
                for l in list_of_courses:
                    if l.C_id==c:
                        print("Course name:",l.C_name)
                s=input("Enter staff id:")
                for l in list_of_User:
                    if l.id==s:
                        l.list_of_courses=c
                        print(l.name)
                    
                    
                
                
                
                
    def main_code(self):
        while True:
            choice = int(input(f"1. Add User:\n"
                               f"2. Add Course:\n"
                               f"3. View User:\n"
                               f"4. View Course:\n"
                               f"5. Search User:\n"
                               f"6. Assign Course:\n"
                               f"7. Exit Program: "))
        
            if choice == 1:
                print("                   ..Adding User..")
                self.adduser()
            
            elif choice == 2:
                print("                   ..Adding Course..")
                self.addcourse()
            elif choice == 3:
                self.viewuser()
            elif choice == 4:
                self.viewcourse()
            elif choice ==5:
                i=input("Enter User Id:")
                self.searchuser(i)
            elif choice==6:
                 self.assigncourse()
            elif choice == 7:
                break
            else:
                print("Enter valid choice:")

if __name__ == "__main__":
    fun = Function()
    print("\n                                    ...................SCHOOL MANAGEMENT SYSTEM...................")
    fun.main_code()