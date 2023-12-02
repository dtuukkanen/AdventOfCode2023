def get_calibration_number(word):
    first_digit = None
    last_digit = None

    for i in range(len(word)):
        if word[i].isdigit():
            if first_digit is None:
                first_digit = word[i]
            last_digit = word[i]

    return int(first_digit + last_digit)


def trebuchet(words):
    calibration_values = []
    calibration_value = 0

    for word in words:
        calibration_values.append(get_calibration_number(word))
        calibration_value += get_calibration_number(word)

    return calibration_value


if __name__ == "__main__":
    with open("input.txt") as input_file:
        words = input_file.readlines()
    print(trebuchet(words))
