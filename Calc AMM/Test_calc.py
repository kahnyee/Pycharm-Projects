import calc

def test_find_min_max():

    input = [5,6,7,4,8,18]
    test = [4,18]

    results = calc.find_min_max(input)
    assert (results == test)
def test_calc_average():

    input = [5, 6, 7, 4, 8, 18]
    test = 8.0

    results = calc.calc_average(input)
    assert (results == test)
def test_calc_median_temperature():

    input = [5, 6, 7, 4, 8, 18]
    test = 6.5

    results = calc.calc_median_num(input)
    assert (results == test)
