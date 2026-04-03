import income

def test_calc_totals_no_rows():
    """ensure thast when there are no rows, the totals are returned as zero"""

    total_income, total_expenses = income.calculate_totals([])
    assert total_income == 0
    assert total_expenses == 0

def test_calc_totals_one_row():
    """ensure that when there is only a single row, the totals reflect that single amount"""
    
    rows = [{"Amount": -150}]

    total_income, total_expenses = income.calculate_totals(rows)

def test_calc_totals_multiple_rows():
    """ensure that when there are several rows, the totals reflect the sum of income and expenses"""
    rows = [{"Amount": -150}, {"Amount": -150}, {"Amount": 50}, {"Amount": 400}]

    total_income, total_expenses = income.calculate_totals(rows)
    assert total_income == 450
    assert total_expenses == 300

# to test, input pytest into the terminal. this will tell vs code to run test anything that begins with test_
# running the module wont output anything because it will just import the previous module, define the functions, then end.

#ALSO never capitalize the names of modules.