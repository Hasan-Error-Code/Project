mark = int(input("Enter a mark 0 to 100: "))

if mark >= 80 and mark <= 100:
    print(f"Result: A+      Grade: 4.00")
elif mark >= 75 and mark < 80:
    print("Result: A        Grade: 3.75")
elif mark >= 70 and mark < 75:
    print("Result: A        Grade: 3.50")
elif mark >= 65 and mark < 70:
    print("Result: B+       Grade: 3.25")
elif mark >= 60 and mark < 65:
    print("Result: B        Grade: 3.00")
elif mark >= 55 and mark < 60:
    print("Result: B-       Grade: 2.75")
elif mark >= 50 and mark < 55:
    print("Result: C+       Grade: 2.50")
elif mark >= 45 and mark < 50:
    print("Result: C        Grade: 2.25")
elif mark >= 40 and mark < 45:
    print("Result: C        Grade: 2.00")
else: 
    print("Result: F        Grade: 0.00")