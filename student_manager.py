students = {}

while True:
    print("\n1. Add  2. View  3. Search  4. Delete  5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        roll = input("Roll no: ")
        students[roll] = input("Name: ")
    elif choice == "2":
        for roll, name in students.items():
            print(roll, name)
    elif choice == "3":
        roll = input("Roll no: ")
        print(students.get(roll, "Not found"))
    elif choice == "4":
        students.pop(input("Roll no: "), None)
    elif choice == "5":
        break
