#Nazim Zerrouki
#11/12/17
#This program will associate five test scores with their respective letters and then calculate the average and print out the letter grade for that average
#It refers to showScores and calcAverage and passes the list of grades to each function
def main():
    grade = input("Enter the grades: ")
    grades = grade.split(',')
    index = 0
    for grade in grades:
        grades[index] = float(grades[index])
        index += 1
        
    showScores(grades)
    calcAverage(grades)
    print()

#showScores will print out the score and its respective letter grade
def showScores(score_list):
    index = 0
    for score in score_list:
        print(score_list[index], 'is', printLetterGrade(score))
        index += 1

#This function will provide a test score's letter grade based on these conditions and return it to the score
def printLetterGrade(score):
    letter_grade = ""
    if score in range(90, 101):
        letter_grade = 'A'
    elif score in range(80, 90):
        letter_grade = 'B'
    elif score in range(70,80):
        letter_grade = 'C'
    elif score in range(60,70):
        letter_grade = 'D'
    elif score < 60:
        letter_grade = 'F'
    return letter_grade

#This function refers to the list and computes the average of scores.
def calcAverage(grade_list):
    idx = 0
    total = 0
    for grade in grade_list:
        total += grade
        idx += 1
        average = total / idx
    print("The average is:", average, "which is the letter grade", printLetterGrade(grade))
main()
    
