# Keywords and Clues
# Generates a letter grade from a number
# Enter a number and then send out a letter

#  We need to use Conditonal Statements (IF / ELSE / ELIF)

grades = [60,70,80,90]  
def gradeBook(gradeScore):
    if gradeScore >= grades[3]:
        print('this student has an A')
    elif gradeScore >= grades[2]: 
        print('this student has a B')
    elif gradeScore >= grades[1]:
        print('this student has a C')
    elif gradeScore >= grades[0]:
        print('this student has a D')
    else:
        print('this student has a F.')

gradeBook(86)
