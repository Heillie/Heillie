#heilliesantana
def calculate_classification(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Healthy Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmi(weight, height, system):
    if system == "imperial":
        weight_kg = weight * 0.453592
        height_m = height * 0.0254
    elif system == "metric":
        weight_kg = weight
        height_m = height
    else:
        return None  # Invalid system

    try:
        bmi = weight_kg / (height_m ** 2)
        return bmi
    except ZeroDivisionError:
        return None
    except Exception as e:
        return str(e)

def main():
    try:
        print("Welcome to the BMI Calculator!")
        system = input("Choose the system (imperial or metric): ").lower()

        weight = float(input("Enter your weight: "))
        height = float(input("Enter your height: "))

        bmi = calculate_bmi(weight, height, system)

        if bmi is not None:
            print("Your BMI is {:.2f}".format(bmi))
            classification = calculate_classification(bmi)
            print("Your classification is:", classification)
        else:
            print("Error: Invalid input or division by zero.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
