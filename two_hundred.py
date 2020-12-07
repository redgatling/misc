def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def concat(a, b):
    return int(str(int(a)) + str(b))


def to_base_n(num: int, n: int) -> str:
    """
    Converts base-10 number to base-n number
    In our case, we use only conversion to base-5
    """
    if num == 0:
        return '0'

    num_base_n = ''

    while num > 0:
        num_base_n += str(num % n)
        num //= n

    return num_base_n[::-1]


def gen_operations():
    """
    This generator creates length-9 sequences of operations
    based on 9-digit numbers
    Example: 420001110 would decode to _ * + + + - - - +
    Result would be 98 * 7 + 6 + 5 + 4 - 3 - 2 - 1 + 0
    This generator skips all operations, that would divide by 0
    """
    sequence_code = 0
    num_to_operation = {'0': add, '1': sub, '2': mult, '3': div, '4': concat}

    while True:
        base_5 = to_base_n(sequence_code, 5)
        sequence_code_string = base_5.zfill(9)

        if int(base_5) % 10 == 3:
            sequence_code += 1
        else:
            sequence = []
            for s in sequence_code_string:
                sequence.append(num_to_operation[s])
            sequence_code += 1
            yield sequence


digits = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
all_operations = gen_operations()
count_of_200 = 0

for opers in all_operations:
    result = digits[0]

    try:
        for i in range(len(opers)):
            result = opers[i](result, digits[i+1])
    except IndexError:
        print("End of operations reached")
        break

    if result == 200:
        count_of_200 += 1

print('Found {} sign combinations, that lead to 200'.format(count_of_200))
