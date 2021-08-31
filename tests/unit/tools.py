from conga_office.tools import activate_conga_office


def test_linear_pattern():
    activate_conga_office(duration=2, speed='turbo')
    assert True


def test_diamond_pattern():
    activate_conga_office(duration=4, speed='normal', pattern='diamond')
    assert True
