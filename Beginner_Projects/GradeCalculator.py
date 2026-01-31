print("Welcome to the Grade Calculator!")
print("This system is for a Canadian grading scale.")


def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 85:
        return 'A'
    elif marks >= 80:
        return 'A-'
    elif marks >= 77:
        return 'B+'
    elif marks >= 73:
        return 'B'
    elif marks >= 70:
        return 'B-'
    elif marks >= 67:
        return 'C+'
    elif marks >= 63:
        return 'C'
    elif marks >= 60:
        return 'C-'
    elif marks >= 57:
        return 'D+'
    elif marks >= 53:
        return 'D'
    elif marks >= 50:
        return 'D-'
    else:
        return 'F'
    
    
def display_menu():
    print("\nMenu:")
    print("1. Add a grade")
    print("2. View grades")
    print("3. Remove a grade")
    print("4: Save grades to file")
    print("5. Exit")
    
grades = []

while True:
    display_menu()
    choice = input("Choose an option (1-5): ").strip()
    
    if choice == "1":
        try:
            label = input("Enter the label for the grade (e.g., Assignment 1, Midterm): ").strip()
            grade = float(input("Enter the grade (0-100): ").strip())
            weight = float(input("Enter the weight of the grade (as a percentage, e.g., 20 for 20%): ").strip())
            if 0 <= grade <= 100 and 0 < weight <= 100:
                grades.append((label, grade, weight))
                print(f'Grade for {label}: {grade} with weight {weight}% added.')
            elif sum(w for _, _, w in grades) + weight > 100:
                print("Total weight exceeds 100%. Please adjust the weights of your grades.")
            else:
                print("Please enter a valid grade between 0 and 100 and/or a valid weight between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    elif choice == "2":
        if not grades:
            print("No grades available.")
        else:
            print("Grades and their corresponding letter grades:")
            for idx, grade in enumerate(grades, start=1):
                label, grade_value, weight = grade
                letter_grade = calculate_grade(grade_value)
                print(f"{idx}. {label}: {grade_value} (Weight: {weight}%) - {letter_grade}")
            if sum(weight for _, _, weight in grades) == 100:
                print("\nFinal Grade Calculation:")
                total_weighted_score = 0
                total_weight = 0
                for label, grade_value, weight in grades:
                    total_weighted_score += grade_value * weight / 100
                    total_weight += weight
                if total_weight > 0:
                    final_grade = total_weighted_score / total_weight * 100
                    final_letter_grade = calculate_grade(final_grade)
                    print(f"Final Grade: {final_grade:.2f}% - {final_letter_grade}")
                else:
                    print("No grades available to calculate final grade.")
        
    elif choice == "3":
        if not grades:
            print("No grades to remove.")
        else:
            print("Grades:")
            for idx, grade in enumerate(grades, start=1):
                print(f"{idx}. {grade}")
            try:
                grade_num = int(input("Enter the grade number to remove: ").strip())
                if 1 <= grade_num <= len(grades):
                    removed_grade = grades.pop(grade_num - 1)
                    print(f'Grade {removed_grade} removed.')
                else:
                    print("Invalid grade number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == "4":
        filename = input("Enter the filename to save grades (e.g., grades): ").strip()
        filename += ".txt"       
        course_name = input("Enter the name of the course: ").strip()
        
        try:
            with open(filename, 'w') as file:
                file.write(f"Course: {course_name}\n")
                for grade in grades:
                    label, grade_value, weight = grade
                    letter_grade = calculate_grade(grade_value)
                    file.write(f"{label}: {grade_value} (Weight: {weight}%) - {letter_grade}\n")
            print(f"Grades saved to {filename}")
        except Exception as e:
            print(f"Error saving grades to file: {e}")
    
    elif choice == "5":
        print("Exiting the Grade Calculator. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")