# CTI-110
# P3HW1 - Debugging
# Homework project
# FREEMAN
# 10/25/2021

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 89
    C_score = 79
    D_score = 69
    


    # User input to find scores

    
    score = int(input('Enter grade: '))

    if  score >= A_score:
        print('Your grade is: A')
    elif (score <= B_score) and (score >= 80):
        print('Your grade is: B')
    elif (score <= C_score) and (score >= 70):
        print ('Your grade is: C')
    elif (score <= D_score) and (score >= 60):
        print ('Your grade is: D')
    else:
        print('Your grade is: F') 







# program start
main()
