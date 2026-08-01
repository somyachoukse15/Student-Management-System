def main():
    greet()
    
    # try:
    while True:
        option= int(input("Enter your choice between 1 to 5: "))
        if option==1:
            view_student_details()
        elif option==2:
            add_new_students()
        elif option==3:
            remove_student()
        elif option==4:
            edit_student()
        elif option==5:
            print("Exiting the program. Good bye!") 
        else:
            print("Invalid option!! Please select a valid option from the menu")
                
    # except Exception as e:
    #     print("Invalid option!! Please select a valid option from the menu",e)

def view_student_details():
    with open("student.txt","r") as file:
        students=file.readlines()
        if not students:
            print("No student found")
        else:
            print("Student details")
            for student in students:
                print(student.strip())

def add_new_students():
    name=input("Enter student's name:")
    age=input("Enter student's age:")
    grade=input("Enter student's grade:")
    
    with open("student.txt","a") as file:
        file.write(f"{name},{age},{grade}\n")
        
def remove_student():
    remove_name=input("Enter the name of student you want to remove: ")
    new_students=[]
    with open("student.txt","r") as file:
        students=file.readlines()
        found=False
        for  student in students:
            name = student.split(",")[0]
            if remove_name!=name:
                new_students.append(student)
            else: 
                found=True
        if found!=True:
            print("Student not found")
        else:
            with open("student.txt","w") as file:
                    file.writelines(new_students)
                    print(new_students)
                    print("Student's name has been succesfully removed")
           
def edit_student():
    updated_name=input("Enter the name of student you want to updated: ") 
    new_students=[]
    with open("student.txt","r") as file:
        students=file.readlines()
        found=-1
        for  student in students:
            name = student.split(",")[0]
            if updated_name==name:
                found=True 
                new_data=get_updated_data_from_user()
                new_students.append(new_data)

            else:
                new_students.append(student)
        if found==-1:
            print("Student not found")
        else:
            with open("student.txt","w") as file:
                    file.writelines(new_students)
                    print(new_students)
                    print("Student's data has been updated sucessfully")


def get_updated_data_from_user():
    updated_name=input("Enter corrected student's name:")
    updated_age=input("Enter corrected student's age:")
    updated_grade=input("Enter corrected student's grade:")
    new_data=f"{updated_name},{updated_age},{updated_grade}\n"

    return new_data

def greet():
    print("#############################WELCOME TO THE STUDENT PORTAL#############################")
    print("Please select an option from the menu below")
    print("Press 1 to see student data")
    print("Press 2 to add more student")
    print("Press 3 to remove student")
    print("Press 4 to edit student")
if __name__=="__main__":
        main()