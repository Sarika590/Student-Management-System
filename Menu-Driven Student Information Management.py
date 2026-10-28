students={}
def add_student():
    roll=input("Enter Roll no:")
    name=input("Enter name:")
    dept=input("Enter Department:")
    students[roll]={"name":name,"Department":dept}
    print("student added successfully.")
def view_student():
    if not students:
        print("No student records found.")
        return 
    print("\n----studebt Records----")
    for roll,data in students.items():
        print("Roll No:",roll,"Name:",data["name"],"Department:",data["Department"])
def search_student():
    roll=input("Enter Roll number to search:")
    if roll in students:
        print(students[roll])
    else:
        print("Student not found")
def delete_student():
    roll=input("Enter Roll number to delete:")
    if roll in students:
        del students[roll]
        print("student deleted succesfully")
    else:
        print("Student not found")
while True:
    print("\n1.Add student")
    print("2.view students")
    print("3.Search students")
    print("4.Delete student")
    print("5.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_student()
    elif choice=="3":
        search_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        print("Exiting...")
        break
    else:
        print("Invalid Choice")