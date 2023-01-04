
def read_from_console(information: list) -> int:
    temp_variable = [
        line
        for line in information
        if "packet loss" in line
    ]
    temp_variable = temp_variable[0].split(",")
    temp_variable = temp_variable[-1].split(" ")
    result = None
    for percent in temp_variable:
        if "%" in percent:
            result = percent[:-3]
            break
    return int(result)
