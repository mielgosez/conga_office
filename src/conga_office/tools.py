import pyautogui
import numpy as np
from conga_office.config.metadata import valid_speed_modes


def get_speed(speed_value: str):
    if speed_value in valid_speed_modes.keys():
        return valid_speed_modes[speed_value]
    else:
        raise ValueError(f'{speed_value} is not a recognized valid value. '
                         f'Valid values are: {", ".join(list(valid_speed_modes.keys()))}')


def validate_duration_and_speed(duration: float, speed: float):
    if duration < speed:
        raise ValueError(f'duration (= {duration} seconds) is smaller than speed (= {speed} seconds).')


def run_linear_pattern(duration: float, speed: str):
    """
    Left to right pattern.
    :param speed:
    :param duration: Duration of mouse movement in seconds.
    :return:
    """
    width, height = pyautogui.size()
    speed_float = get_speed(speed_value=speed)
    validate_duration_and_speed(duration=duration, speed=speed_float)
    previous = 0
    for _ in np.arange(0, duration, speed_float):
        pyautogui.moveTo(previous, height / 2, duration=speed_float)
        if previous == 0:
            previous = width
        else:
            previous = 0


def run_diamond_pattern(duration: float, speed: str):
    """
    Left to right pattern.
    :param speed:
    :param duration: Duration of mouse movement in seconds.
    :return:
    """
    width, height = pyautogui.size()
    speed_float = get_speed(speed_value=speed)
    validate_duration_and_speed(duration=duration, speed=speed_float)
    previous_x = 0
    previous_y = height/2
    for _ in np.arange(0, duration, speed_float):
        pyautogui.moveTo(previous_x, previous_y, duration=speed_float)
        if (previous_x == 0) & (previous_y == height/2):
            # Go North
            previous_x = width/2
            previous_y = height
        elif (previous_x == width/2) & (previous_y == height):
            # Go East
            previous_x = width
            previous_y = height/2
        elif (previous_x == width) & (previous_y == height/2):
            # Go South
            previous_x = width/2
            previous_y = 0
        else:
            # Go West
            previous_x = 0
            previous_y = height / 2


def run_random_pattern(duration: float, speed: str):
    """

    :param duration:
    :param speed:
    :return:
    """
    width, height = pyautogui.size()
    speed_float = get_speed(speed_value=speed)
    validate_duration_and_speed(duration=duration, speed=speed_float)
    for _ in np.arange(0, duration, speed_float):
        x = np.random.uniform(0, width)
        y = np.random.uniform(0, height)
        pyautogui.moveTo(x, y, duration=speed_float)


def run_circular_pattern(duration: float, speed: str):
    """

    :param duration:
    :param speed:
    :return:
    """
    width, height = pyautogui.size()
    speed_float = get_speed(speed_value=speed)
    radius = min(width, height)/2
    validate_duration_and_speed(duration=duration, speed=speed_float)
    for _ in np.arange(0, duration, speed_float):
        for i in range(100):
            x = width/2 + radius*np.cos(2*np.pi*i/100)
            y = height/2 + radius*np.sin(2*np.pi*i/100)
            pyautogui.moveTo(x, y, duration=speed_float/100)


def activate_conga_office(duration: float, pattern: str = 'linear', speed: str = 'normal'):
    """

    :param speed: Speed to move from one point to the other:
        - normal: 1 seconds
        - slow: 2 seconds
        - turbo: 0.1 seconds
    :param duration: Duration of pattern. Must be higher to 1.
    :param pattern: Pattern of conga-office:
        - linear: left-to-right
        - diamond: west-north-east-south cycle.
        - random: move randomly across the screen.
        - circle: mouse moves in a perfect circle.
    :return:
    """
    # Validation
    if pattern == 'linear':
        run_linear_pattern(duration=duration, speed=speed)
    elif pattern == 'diamond':
        run_diamond_pattern(duration=duration, speed=speed)
    elif pattern == 'random':
        run_random_pattern(duration=duration, speed=speed)
    elif pattern == 'circular':
        run_circular_pattern(duration=duration, speed=speed)
    else:
        raise NotImplementedError(f'{pattern} has not been implemented as a pattern.')


def find_teams():
    _, height = pyautogui.size()
    pyautogui.click(0, height)
    pyautogui.typewrite('teams')
    pyautogui.typewrite(['enter'])
