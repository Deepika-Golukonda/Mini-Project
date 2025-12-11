
students =[]
def add_student(name,age,course):
  student={"name":name,"age": age,"course":course}
  students.append(student)
  print("Student added!")
def view_students():
    for s in students:
        print(s)
def search_student(name):
    for s in students:
        if s["name"] == name:
            print("Found:", s)
            return
    print("Student not found")
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")
        course = input("Course: ")
        add_student(name, age, course)

    elif choice == "2":
        view_students()
    
    elif choice == "3":
        name = input("Enter name to search: ")
        search_student(name)
    
    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
