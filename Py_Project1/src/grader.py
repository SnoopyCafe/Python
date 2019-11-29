''' Write code that asks the user to enter a 
 numeric score (0-100). In response, it 
 should print out the score and corresponding 
 letter grade, according to the table below.
 
 Score    Grade
 >= 90    A
 [80-90)    B
 [70-80)    C
 [60-70)    D
 < 60    F
 '''

inp = input("Score?")
if inp:
    output(int(inp))
else:
    print("Nothing entered.")

def output(score):
    grade = ''
    if score >= 90:
        grade = 'A'
    if score >= 80 and score < 90:
        grade = 'B'
    if score >= 70 and score < 80:
        grade = 'C'
    if score >= 60 and score < 70:
        grade = 'D'
    if score < 60:
        grade = 'F'
    
    print(grade)
    return 