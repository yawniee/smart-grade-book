# Using data structures such as:-
student_database = {}  # Dictionary: { student_id: {name: str, scores: list} }
all_subjects = set()   # Set to track unique subjects

# Global configuration (Immutable scale)
GRADE_CUTOFFS = (90, 80, 70, 60) # Tuples for fixed rules

# Defining a variable which generates an id
def generate_id(name):
    return name[0:3].upper() + "-2026"
    pass

# Defining a variable that gives student a letter grade
def calculate_letter_grade(average):
    if average >=90:
        return 'A'
    elif average >=80:
        return 'B'
    elif average >=70:
        return 'C'
    else:
        return 'F'
    pass

#The main variable by which we can add a student to our gradebook
def add_student():
    print("\n--- Add New Student ---")
    name = input("Enter student's full name: ")
    student_id = generate_id(name)
    student_scores = []
    
    while True:
        subject = input("Enter subject name: ").strip()
        all_subjects.add(subject) # Adding to the unique set
        while True:
        # Using try-except blocks in which we ask for a score, cast it to a float, and append to the scores list.
        # If casting fails, it prints an error and asks for the score again.
            try:
                marks=float(input(f"Enter marks for {subject}:"))
                break
            except ValueError:
                print("[!] Invalid score. Please enter a number")
        student_scores.append((subject, marks))
        print(f"Successfully added {name} with a score of {marks} in {subject}")
        another=input(f"Add another score for {name}? (y/n):").lower().strip()
        if another=='n':
            break

    # Save to dictionary
    student_database[student_id] = {
        "name": name,
        "scores": student_scores
    }
    print(f"\nStudent added successfully with ID: {student_id}")

def view_report():
    print("\n================ CLASS REPORT ================")
    if not student_database:
        print("No student records found.")
        print("==============================================\n")
        return
    for student_id, student_info in student_database.items():
        name=student_info["name"]
        scores_list=student_info["scores"]

        if len(scores_list)==0:
            average=0.0
            letter_grade='F'
        else:
            total_marks=0
        for subject, marks in scores_list:
            total_marks+=marks
        average =total_marks/len(scores_list)
        letter_grade=calculate_letter_grade(average)
        print(f"ID: {student_id} | Name: {name} | Final Grade: {letter_grade} (Avg: {average})")
        
    # Calculate each student's average, call calculate_letter_grade(),
    # and print their record using a formatted f-string.
    
    print("----------------------------------------------")
    print(f"Total Unique Subjects Taught: {all_subjects}")
    print("==============================================\n")

def main():
    while True:
        print("=== SMART GRADEBOOK INITIALIZED ===")
        print("1. Add Student\n2. View Class Report\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_report()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

# This triggers the program to run
if __name__ == "__main__":
    main()
