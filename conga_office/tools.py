import pyautogui
import numpy as np
import json


def get_speed(speed_value: str):
    with open('./config/metadata.json', 'rb') as fp:
        metadata_file = json.load(fp)
    if speed_value in metadata_file['valid_speed_modes'].keys():
        return metadata_file['valid_speed_modes'][speed_value]
    else:
        raise ValueError(f'{speed_value} is not a recognized valid value. '
                         f'Valid values are: {", ".join(list(metadata_file["valid_speed_modes"].keys()))}')


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
        - circle: mouse moves in a perfect circle.
    :return:
    """
    # Validation
    if pattern == 'linear':
        run_linear_pattern(duration=duration, speed=speed)
    elif pattern == 'diamond':
        run_diamond_pattern(duration=duration, speed=speed)
    else:
        raise NotImplementedError(f'{pattern} has not been implemented as a patter.')
