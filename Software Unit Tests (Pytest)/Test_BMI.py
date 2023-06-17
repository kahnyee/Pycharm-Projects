from bmi import calculate_bmi

# Write test cases using pytest
def test_bmi_class_underweight():
    # Test case for underweight BMI class
    bmi_class, classification_value = calculate_bmi(1.7, 50)
    assert bmi_class == "Underweight"
    assert classification_value == -1

def test_bmi_class_normal():
    # Test case for normal BMI class
    bmi_class, classification_value = calculate_bmi(1.7, 65)
    assert bmi_class == "Normal"
    assert classification_value == 0

def test_bmi_class_overweight():
    # Test case for overweight BMI class
    bmi_class, classification_value = calculate_bmi(1.7, 80)
    assert bmi_class == "Overweight"
    assert classification_value == 1