from src.conga_office.tools import activate_conga_office


def test_linear_pattern():
    activate_conga_office(duration=1, speed='turbo')
    assert True


def test_diamond_pattern():
    activate_conga_office(duration=1, speed='normal', pattern='diamond')
    assert True


def test_random_pattern():
    activate_conga_office(duration=1, speed='normal', pattern='random')
    assert True


def test_circular_pattern():
    activate_conga_office(duration=3, speed='normal', pattern='circular')
    assert True
