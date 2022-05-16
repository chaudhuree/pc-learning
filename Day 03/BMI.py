height = float(input("what is your height (in inches):"))
weight = float(input("what is your weight (in pound):"))
bmi = round(weight*703/height**2, 2)
if bmi < 16:
    category = "Severely Underweight"
elif bmi < 18.4:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal"
elif bmi < 29.9:
    category = "Overweight"
elif bmi < 34.0:
    category = 'Moderately obese'
elif bmi < 39.9:
    category = 'Severely obese'
else:
    category = 'Very severely obese'
print(f"Your BMI is:,{bmi},'and your category is:',{category}")
