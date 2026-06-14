age = int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")

test_score = int(input("Enter your test score"))
attendance_percentage = int(input("Enter your attendance percentage"))
if test_score >= 70 and attendance_percentage >= 80:
    print("Congrats you passed the class!")
else:
    print("Sorry but you failed.")

has_student_id = input("Do you have a student ID? (yes/no): ").lower()
has_library_card = input("Do you have a library card? (yes/no): ").lower()
if has_student_id == "yes" or has_library_card == "yes":
    print("You may enter the library.")
else:
    print("Access denied. You need a student ID or library card.")

is_banned = input("Are you banned from the system? (yes/no): ").lower()
if not is_banned == "yes":
    print("You may access the system.")
else:
    print("Access denied due to ban.")

gpa = float(input("Enter your GPA: "))
volunteer_hours = int(input("Enter your volunteer hours: "))
leadership = input("Do you hold a leadership role? (yes/no): ").lower()
if gpa >= 3.5 and (volunteer_hours >= 50 or leadership == "yes"):
    print("You qualify for the scholarship.")
else:
    print("You do not qualify for the scholarship.")