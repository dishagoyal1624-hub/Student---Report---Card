name = input("Enter your name : ")
rollno = int(input("Enter your roll no : "))
English = int(input("Enter your marks in English : "))
Maths= int(input("Enter your marks in Maths : "))
Science = int(input("Enter your marks in Science : "))
Computer = int(input("Enter your marks in Computer : "))
Hindi = int(input("Enter your marks in Hindi : "))
print("\n--------Student Report Card--------")
print("\n-----------------------------------")
print(f"Name : {name}")
print(f"Roll No. : {rollno}")
print("\n-----------------------------------")
print(f"English : {English}")
print(f"Maths : {Maths}")
print(f"Science : {Science}")
print(f"Computer : {Computer}")
print(f"Hindi : {Hindi}")
print("\n-----------------------------------")
obtained_marks = English + Maths + Science + Computer + Hindi
print(f"Obtained Marks : {obtained_marks}")
TotalMarks = 500
print(f"Total Marks : {TotalMarks}")
Percentage = (obtained_marks/TotalMarks)*100
print(f"Percentage : {Percentage : .2f}%")
if English < 33 or Maths < 33 or Science < 33 or Computer < 33 or Hindi < 33:
    print("Grade : Fail")
elif Percentage >= 90 :
    print("Grade : A+")
elif Percentage >= 80 and Percentage <= 89:
    print("Grade : A")
elif Percentage >= 70 and Percentage <= 79:
    print("Grade : B")
elif Percentage >= 60 and Percentage <= 69:
    print("Grade : C")
elif Percentage >= 50 and Percentage <= 59:
    print("Grade : D")
else:
    print("Grade : Fail")
if English < 33 or Maths < 33 or Science < 33 or Computer < 33 or Hindi < 33:
    print("Result : Fail")
else:
    print("Result : Pass")