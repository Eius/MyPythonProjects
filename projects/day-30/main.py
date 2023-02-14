try:
    height = float(input("Height: "))
    weight = float(input("Weight: "))
    if height > 3:
        raise ValueError("Human height should not be over 3 meters.")

except ValueError as e:
    print(e)

else:
    bmi = weight / pow(height, 2)
    print(f"Your BMI is {bmi}")