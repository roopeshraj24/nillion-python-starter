#Nada Program to Calculate and Compare the Grades of Two Students for each of their subjects
from nada_dsl import *

def get_grade(marks):
    if marks >= 90:
        return SecretInteger(5)  # Grade A
    elif marks >= 80:
        return SecretInteger(4)  # Grade B
    elif marks >= 70:
        return SecretInteger(3)  # Grade C
    elif marks >= 60:
        return SecretInteger(2)  # Grade D
    else:
        return SecretInteger(1)  # Grade E

def nada_main():

    # Define the party
    party1 = Party(name="Party1")

    # Define the input secret integers for students' marks
    student1_marks = SecretInteger(Input(name="student1_marks", party=party1))
    student2_marks = SecretInteger(Input(name="student2_marks", party=party1))

    # Assign grades based on marks
    student1_grade = get_grade(student1_marks)
    student2_grade = get_grade(student2_marks)

    # Compare the grades
    comparison_result = student1_marks - student2_marks

    # Define the outputs
    output_student1_grade = Output(student1_grade, "student1_grade", party1)
    output_student2_grade = Output(student2_grade, "student2_grade", party1)
    output_comparison = Output(comparison_result, "grade_comparison", party1)

    return [output_student1_grade, output_student2_grade, output_comparison]
