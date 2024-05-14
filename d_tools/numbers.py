from random import randint


def generate_number_code_str(num_digits: int = 6) -> str:
    lower_bound = 10 ** (num_digits - 1)
    upper_bound = (10 ** num_digits) - 1

    random_number = randint(lower_bound, upper_bound)

    return str(random_number)


def generate_number_code_int(num_digits: int = 6) -> int:
    lower_bound = 10 ** (num_digits - 1)
    upper_bound = (10 ** num_digits) - 1

    random_number = randint(lower_bound, upper_bound)

    return random_number
