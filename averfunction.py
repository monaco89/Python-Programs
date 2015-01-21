#Nick Monaco
#CMPT 101-01
#Average with Functions

def grades():
    grade1= eval(input("Grade of test 1:"))
    grade2= eval(input("Grade of test 2:"))
    grade3= eval(input("Grade of test 3:"))
    grade= grade1+grade2+grade3
    return grade

def average(grade):
    aver= grade/3
    return aver

def main():
    again='y'
    while again.lower()=='y':
        grade=grades()
        aver= average(grade)
        if aver>=90:
            grade='A'
        elif aver>=80:
            grade='B'
        elif aver>=70:
            grade='C'
        elif aver>=65:
            grade='D'
        else:
            grade='F'
        print("grade is:",grade)
        again=input("another?(y/n):")

main()
