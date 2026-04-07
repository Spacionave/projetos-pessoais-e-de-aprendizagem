# List to store student names
students = []

# List to store students' grades (each student has a list of 3 grades)
grades = []


# Function to register a new student
def registerStudent():
    # Ask for the student's name
    name = input("Enter the student's name: ")
    
    # Ask for the three grades
    g1 = float(input("Enter the 1st grade: "))
    g2 = float(input("Enter the 2nd grade: "))
    g3 = float(input("Enter the 3rd grade: "))

    # Add the student's name to the list
    students.append(name)
    
    # Add the grades as a list inside the "grades" list
    grades.append([g1, g2, g3])


# Function to list all registered students
def listStudents():
    # Check if there are no students
    if len(students) == 0:
        print("No students registered")
    else:
        # Loop through all students
        for i in range(len(students)):
            # Show index, name and grades
            print(f"{i+1} - {students[i]} - grades: {grades[i]}")


# Function to remove a student
def removeStudent():
    # Check if there are students
    if len(students) == 0:
        print("No students registered")
    else:
        # Show the list of students
        listStudents()
        
        # Ask which student to remove
        index = int(input("Enter the student number to remove: ")) - 1
        
        # Check if index is valid
        if 0 <= index < len(students):
            # Remove student and their grades
            students.pop(index)
            grades.pop(index)
            print("Student removed successfully!")


# Function to calculate and show the average grade of each student
def showAverage():
    # Check if there are students
    if len(students) == 0:
        print("No students registered")
    else:
        # Loop through students
        for i in range(len(students)):
            # Calculate the average of the 3 grades
            average = sum(grades[i]) / 3
            
            # Show student name and average
            print(f"{students[i]} - average: {average:.2f}")


# Function to show student classification based on average
def showClassification():
    # Check if there are students
    if len(students) == 0:
        print("No students registered")
    else:
        # Loop through students
        for i in range(len(students)):
            # Calculate the average
            average = sum(grades[i]) / 3

            # Check classification
            if average >= 8:
                print(f"{students[i]} - EXCELLENT")
            elif average >= 6:
                print(f"{students[i]} - GOOD")
            elif average >= 5:
                print(f"{students[i]} - REGULAR")
            else:
                print(f"{students[i]} - FAILED")


# Main program loop (menu)
while True:
    print("\n=========== MENU ===========")
    print("1 - Register student")
    print("2 - List students")
    print("3 - Remove student")
    print("4 - Show student average")
    print("5 - Show student classification")
    print("6 - Exit")

    # Ask user for an option
    option = input("Enter your option: ")

    # Call the corresponding function
    if option == "1":
        registerStudent()
    elif option == "2":
        listStudents()
    elif option == "3":
        removeStudent()
    elif option == "4":
        showAverage()
    elif option == "5":
        showClassification()
    elif option == "6":
        print("End of program")
        break  # Exit the program
