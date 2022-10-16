from Classes.Input import request_int, request_float, has_range, is_in_range, is_between_range, value_out_of_range, request_valid_int, request_valid_float

test = []
for index in range(22):
    test.insert(index, 0)
    match index:
        case 0:
            passed = False
            while not passed:
                try:
                    print("just press enter:")
                    defaultInt = 0
                    msg = f"Invalid int passed will use {defaultInt}!"
                    test[index] = request_int("enter an integer value:  ", msg, defaultInt)
                    if test[index] == 0:
                        if input(f"Did it reply with the exception message \"{msg}\" (Y/N)? ").lower() in ["y"]:
                            passed = True
                except:
                    print("Pleane enter an actual integer value!")
        case 1:
            passed = False
            while not passed:
                try:
                    print("enter a valid value:")
                    defaultInt = 0
                    msg = f"Invalid int passed will use {defaultInt}!"
                    test[index] = request_int("enter an integer value:  ", msg, defaultInt)
                    if input(f"Did it reply with the exception message \"{msg}\" (Y/N)? ").lower() in ["n"]:
                        passed = True
                except:
                    print("Pleane enter an actual integer value!")
        case 2:
            passed = False
            while not passed:
                try:
                    print("just press enter:")
                    defaultFloat = 0.5
                    msg = f"Invalid int passed will use {defaultFloat}!"
                    test[index] = request_float("enter a float value:  ", msg, defaultFloat)
                    if test[index] == 0:
                        if input(f"Did it reply with the exception message \"{msg}\" (Y/N)? ").lower() in ["y"]:
                            passed = True
                except:
                    print("Pleane enter an actual float value!")
        case 3:
            passed = False
            while not passed:
                try:
                    print("enter a valid value:")
                    defaultFloat = 0.5
                    msg = f"Invalid int passed will use {defaultFloat}!"
                    test[index] = request_float("enter a float value:  ", msg, defaultFloat)
                    if input(f"Did it reply with the exception message \"{msg}\" (Y/N)? ").lower() in ["n"]:
                        passed = True
                except:
                    print("Pleane enter an actual float value!")
        case 4:
            passed = False
            try:
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = has_range(minFloat, maxFloat)
                passed = True
            except:
                passed = False
        case 5:
            passed = False
            try:
                minFloat = ""
                maxFloat = 0.5
                test[index] = has_range(minFloat, maxFloat)
                passed = False
            except:
                passed = True
        case 6:
            passed = False
            try:
                valFloat = -1.0
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = is_in_range(valFloat, minFloat, maxFloat)
                passed = False
            except:
                passed = True
        case 7:
            passed = False
            try:
                valFloat = -0.5
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = is_in_range(valFloat, minFloat, maxFloat)
                passed = True
            except:
                passed = False
        case 8:
            passed = False
            try:
                valFloat = 0.0
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = is_in_range(valFloat, minFloat, maxFloat)
                passed = True
            except:
                passed = False
        case 9:
            passed = False
            try:
                valFloat = 0.5
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = is_in_range(valFloat, minFloat, maxFloat)
                passed = True
            except:
                passed = False
        case 10:
            passed = False
            try:
                valFloat = 1.0
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = is_in_range(valFloat, minFloat, maxFloat)
                passed = False
            except:
                passed = True
        case 11:
            passed = False
            try:
                valFloat = -1.0
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = is_between_range(valFloat, minFloat, maxFloat)
                passed = False
            except:
                passed = True
        case 12:
            passed = False
            try:
                valFloat = -0.5
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = is_between_range(valFloat, minFloat, maxFloat)
                passed = False
            except:
                passed = True
        case 13:
            passed = False
            try:
                valFloat = 0.0
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = is_between_range(valFloat, minFloat, maxFloat)
                passed = True
            except:
                passed = False
        case 14:
            passed = False
            try:
                valFloat = 0.5
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = is_between_range(valFloat, minFloat, maxFloat)
                passed = False
            except:
                passed = True
        case 15:
            passed = False
            try:
                valFloat = 1.0
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = is_between_range(valFloat, minFloat, maxFloat)
                passed = False
            except:
                passed = True
        case 16:
            passed = False
            try:
                minFloat = ""
                maxFloat = ""
                test[index] = value_out_of_range(minFloat, maxFloat)
                passed = False
            except:
                passed = True
        case 17:
            passed = False
            try:
                minFloat = ""
                maxFloat = 0.5
                test[index] = value_out_of_range(minFloat, maxFloat)
                passed = False
            except:
                passed = True
        case 18:
            passed = False
            try:
                minFloat = -0.5
                maxFloat = ""
                test[index] = value_out_of_range(minFloat, maxFloat)
                passed = False
            except:
                passed = True
        case 19:
            passed = False
            try:
                minFloat = -0.5
                maxFloat = 0.5
                test[index] = value_out_of_range(minFloat, maxFloat)
                passed = False
            except:
                passed = True

        case 20:
            test[index] = request_valid_int("enter an integer value:  ", "Invalid int passed will use 0!", 0, -2, 2)
        case 21:
            test[index] = request_valid_float("enter an float value:  ", "Invalid int passed will use 0!", 0, -2, 2)
    print(f"{index})  {test[index]}")
