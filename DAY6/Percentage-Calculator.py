marks1 = float(input("Enter Maths marks:"))
marks2 = float(input("Enter English marks:"))
marks3 = float(input("Enter Bengali marks:"))
marks4 = float(input("Enter History marks:"))
marks5 = float(input("Enter Geography marks:"))

total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = total / 5

print("total marks:", total)
print("total percentage:", percentage,"%")