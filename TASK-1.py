#STUDENT MARKS,PERCENTAGE AND GRADE
name=input("enter student name:")
n=int(input("enter no. of subjects:"))
total=0
for i in range(1,n+1):
    mark=float(input(f"enter mark for subject{i}:"))
    total+=mark
    percentage=total/n
    if percentage>=90:
        grade="A+"
        performance="outstanding"
    elif percentage>=80:
        grade="A"
        performance="excellent"
    elif percentage>=80:
        grade="B"
        performance="very good"
    elif percentage>=80:
        grade="C"
        performance="good"
    elif percentage>=80:
        grade="D"
        performance="average"
    else:
        grade="F"
        performance="needs improvement"
print("\n---ACADEMIC PERFORMANCE---")
print("student name:",name)
print("total marks:",total)
print("percentage:",round(percentage,2),"%")
print("grade:",grade)
print("performance:",performance)
