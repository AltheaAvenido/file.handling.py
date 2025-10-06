import os

doc_path = os.path.expanduser("~/Documents/StudentRecords")

if not os.path.exists(doc_path):
    os.makedirs(doc_path)

def save_student_record():
    s = input("Student No: ")
    l = input("Last Name: ")
    f = input("First Name: ")
    m = input("Middle Initial: ")
    p = input("Program: ")
    a = input("Age: ")
    g = input("Gender: ")
    b = input("Birthday: ")
    c = input("Contact No: ")

    data = (
        f"\nStudent No: {s}\n"
        f"Full Name: {l}, {f} {m}.\n"
        f"Program: {p}\n"
        f"Age: {a}\n"
        f"Gender: {g}\n"
        f"Birthday: {b}\n"
        f"Contact No: {c}\n"
    )


    file_path = os.path.join(doc_path, f"{s}.txt")
    with open(file_path, "w") as file:
        file.write(data)
        print("✅ Record saved successfully.")
        
    print(file_path)

def open_student_record():
    print("\n=== Open Student Record ===")
    s = input("Enter Student No: ")
    file_path = os.path.join(doc_path, f"{s}.txt")

    try:
        with open(file_path, "r") as file:
            print("\n--- Student Record ---")
            print(file.read())
    except FileNotFoundError:
        print("❌ Student record not found.")


while True:
    print("\n===== Student Records Menu =====")
    print("1. Register Student")
    print("2. Open Student Record")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        continue

    if choice == 1:
        save_student_record()
    elif choice == 2:
        open_student_record()
    elif choice == 3:
        print("Goodbye! Thank you.")
        break
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
