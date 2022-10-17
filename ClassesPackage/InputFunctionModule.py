# InputFunctionModule.py

def request_int(question, exception_message, default_int):
    try:
        value = int(input(question))
    except ValueError:
        if exception_message != "":  print(exception_message)
        value = default_int
    finally:
        return value

def request_float(question, exception_message, default_float):
    try:
        value = float(input(question))
    except ValueError:
        if exception_message != "":  print(exception_message)
        value = default_float
    finally:
        return value

def has_range(min_value, max_value):
    return (type(min_value) is float) or (type(max_value) is float)

def is_in_range(value, min_value, max_value):
    if has_range(min_value, max_value):
        if (type(min_value) is float) and (type(max_value) is float):
            return (value >= min_value) and (value <= max_value)
        elif type(max_value) is float:
            return (value <= max_value)
        elif type(min_value) is float:
            return (value >= min_value)
    else:
        return False

def is_between_range(value, min_value, max_value):
    if has_range(min_value, max_value):
        if (type(min_value) is float) and (type(max_value) is float):
            return (value > min_value) and (value < max_value)
        elif type(max_value) is float:
            return (value < max_value)
        elif type(min_value) is float:
            return (value > min_value)
    else:
        return False

def value_out_of_range(min_value, max_value):
    if has_range(min_value, max_value):
        if type(min_value) is float:
            return min_value - 1
        else:
            return max_value + 1
    else:
        return 0.0

def request_valid_int(question, exception_message, default_int, min_int, max_int):
    if has_range(min_int, max_int):
        value = value_out_of_range(min_int, max_int)
        while not is_in_range(value, min_int, max_int):
            value = request_int(question, exception_message, default_int)
            if (value == default_int) and not is_in_range(value, min_int, max_int):
                if exception_message != "":  print(exception_message)
    else:
        value = request_int(question, exception_message, default_int)
    return value

def request_valid_float(question, exception_message, default_float, min_float, max_float):
    if has_range(min_float, max_float):
        value = value_out_of_range(min_float, max_float)
        while not is_in_range(value, min_float, max_float):
            value = request_float(question, exception_message, default_float)
            if (value == default_float) and not is_in_range(value, min_float, max_float):
                if exception_message != "":  print(exception_message)
    else:
        value = request_float(question, exception_message, default_float)
    return value