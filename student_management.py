import json

students = []

# -------- FILE HANDLING --------
def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except:
        students = []

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)


# -------- FUNCTIONS --------
def add_student():
    id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {
        "id": id,
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_data()
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found")
        return

    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}")


def search_student():
    search_id = input("Enter Student ID to search: ")
    for s in students:
        if s["id"] == search_id:
            print(f"Found: {s}")
            return
    print("Student not found")


def update_student():
    search_id = input("Enter Student ID to update: ")
    for s in students:
        if s["id"] == search_id:
            s["name"] = input("Enter new name: ")
            s["marks"] = input("Enter new marks: ")
            save_data()
            print("Updated successfully!")
            return
    print("Student not found")


def delete_student():
    search_id = input("Enter Student ID to delete: ")
    for s in students:
        if s["id"] == search_id:
            students.remove(s)
            save_data()
            print("Deleted successfully!")
            return
    print("Student not found")


# -------- MENU --------
def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


# -------- MAIN PROGRAM --------
load_data()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
