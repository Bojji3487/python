while True:
    try:
        weight = float(input("Enter weight (kg): "))
        if weight <= 0:
            print("Weight must be positive. Try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Enter a number (e.g., 70).")

while True:
    try:
        height = float(input("Enter height (m): "))
        if height <= 0:
            print("Height must be positive. Try again.")
            continue
        bmi = weight / (height ** 2)
        print(f"Your BMI: {bmi:.2f}")
        break
    except ValueError:
        print("Invalid input. Enter a number (e.g., 1.75).")