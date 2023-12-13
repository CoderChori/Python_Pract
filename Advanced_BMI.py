weight = int(input("Enter weight in KG: "))
height = float(input("Enter height in meters: "))
BMI = weight / (height ** 2)
print("Your BMI is:", BMI)
if BMI < 16.5:
  print(f"Your BMI is: {BMI}, you are severely underweight.")
elif BMI >= 16 and BMI < 16.9:
  print(f"Your BMI is: {BMI}, you are underweight.")
elif BMI >= 17 and BMI < 18.4:
  print(f"Your BMI is: {BMI}, you are underweight(Mild).")
elif BMI >= 18.5 and BMI < 24.9:
  print(f"Your BMI is: {BMI}, you are in Normal weight range.")
elif BMI > 25:
  print(f"Your BMI is: {BMI}, you are Over weight.")
  
