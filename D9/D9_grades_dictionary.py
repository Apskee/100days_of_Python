#Goal of this excercise is to create a dictionary and mark the students depending on the  score they achieved
#Marks:
#Scores 91 - 100: Grade = "Outstanding"

#Scores 81 - 90: Grade = "Exceeds Expectations"

#Scores 71 - 80: Grade = "Acceptable"

#Scores 70 or lower: Grade = "Fail"


##### SOLUTION #####

#List with scores
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#Empty list that will store the marks
student_grades = {}

#For loop, looping through each student, getting their score and putting them into corresponding mark.
for student in student_scores:
    if student_scores[student] >= 91:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    

print(student_grades)