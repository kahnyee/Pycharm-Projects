import employee_info

def test_get_employees_by_age_range():
    test = [
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]
    results = employee_info.get_employees_by_age_range(30,40)
    assert (results == test)
def test_calculate_average_salary():
    test = 60166
    results = int(employee_info.calculate_average_salary())
    assert (results == test)
def test_get_employees_by_dept():
    test = [
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]
    results = employee_info.get_employees_by_dept('Engineering')
    assert (results == test)
