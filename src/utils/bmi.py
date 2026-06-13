def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100

    if height_m <= 0:
        return 0

    return round(weight / (height_m ** 2), 2)


def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    if bmi < 25:
        return "Normal"

    if bmi < 30:
        return "Overweight"

    return "Obese"