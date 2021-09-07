import os

from src.conga_office.tools import activate_conga_office, send_bs_via_teams, send_bs_via_slack


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
    activate_conga_office(duration=1, speed='normal', pattern='circular')
    assert True


def test_teams_bs_generator():
    send_bs_via_teams(os.environ['CONTACT_ID'], 5, 2)
    assert True


def test_slack_bs_generator():
    send_bs_via_slack(contact_id='Test Name', number_of_bs_statements=2, intervals_in_secs=2)
    assert True
