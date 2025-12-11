# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
students = []

def add_student(name, age, course):
    student = {"name": name, "age": age, "course": course}
    students.append(student)
    print("Student added!")


def view_students():
    if not students:
        print("No students yet.")
    for s in students:
        print(s)


def search_student(name):
    for s in students:
        if s["name"] == name:
            print("Found:", s)
            return
    print("Student not found")


def save_to_file():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['name']},{s['age']},{s['course']}\n")
    print("Saved to file!")


def load_from_file():
    students.clear()
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, age, course = line.strip().split(",")
                students.append({"name": name, "age": age, "course": course})
        print("Data loaded!")
    except FileNotFoundError:
        print("No file found!")


# -----------------------
# MAIN MENU LOOP
# -----------------------
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    print("5. Save to File")
    print("6. Load from File")

    choice = input("Enter choice: ").strip()

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

    elif choice == "5":
        save_to_file()

    elif choice == "6":
        load_from_file()

    else:
        print("Invalid choice!")
