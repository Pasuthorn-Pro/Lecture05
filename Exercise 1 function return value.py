def is_armstrong(number):
    number_str = str(number)

    num_digits = len(number_str)

    total = 0

    for digit in number_str:
        total += int(digit) ** num_digits

    if total == number:
        output = " + ".join(f"{int(digit)}^{num_digits}" for digit in number_str)
        
        print(f"{number} = {output}")
        return True
    else:
        return False

print(is_armstrong(371))