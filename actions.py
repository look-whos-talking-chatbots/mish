"""
File contains the generic and custom action functions for mish bot.
"""


def append_change_benefit(user):
    try:
        variable = user['params']['evoke']['change']['benefit']['last']
    except:
        variable = None

    try:
        variable_list = user['params']['evoke']['change']['benefit']['list']
    except:
        variable_list = []

    if variable is not None and variable not in variable_list:
        variable_list.append(variable)

    return variable_list


def append_change_downside(user):
    try:
        variable = user['params']['evoke']['change']['downside']['last']
    except:
        variable = None

    try:
        variable_list = user['params']['evoke']['change']['downside']['list']
    except:
        variable_list = []

    if variable is not None and variable not in variable_list:
        variable_list.append(variable)

    return variable_list


def count_focus_correct(user):
    count = 0

    try:
        if user['params']['multipleChoice']['one'] == 'false':
            count += 1
    except:
        pass

    try:
        if user['params']['multipleChoice']['two'] == 'c':
            count += 1
    except:
        pass

    try:
        if user['params']['multipleChoice']['three'] == 'false':
            count += 1
    except:
        pass

    return count


def count_change_benefit(user):
    count = 0

    try:
        count = len(user['params']['evoke']['change']['benefit']['list'])
    except:
        pass

    return count


def count_change_downside(user):
    count = 0

    try:
        count = len(user['params']['evoke']['change']['downside']['list'])
    except:
        pass

    return count
