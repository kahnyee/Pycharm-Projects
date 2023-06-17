import price_info

def test_total_cost_shopping():

    test = 46.75
    results = price_info.total_cost_shopping()

    assert (results == test)
def test_cost_of_fruit():

    test = 12.0

    results = price_info.cost_of_fruits('apple',10)

    assert (results == test)
