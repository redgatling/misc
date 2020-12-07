
def check_last(s1, s2):
    return (s1 == '(' and s2 == ')') or (s1 == '[' and s2 == ']') or (s1 == '{' and s2 == '}')


def bracket_parser(sequence):
    bracket_stack = []

    for sym in sequence:
        print(bracket_stack)
        bracket_stack.append(sym)
        if len(bracket_stack) > 1:
            if check_last(bracket_stack[-2], bracket_stack[-1]):
                bracket_stack.pop()
                bracket_stack.pop()
        if len(bracket_stack) >= 1:
            if bracket_stack[-1] == '}' or bracket_stack[-1] == ')' or bracket_stack[-1] == ']':
                return False

    return len(bracket_stack) == 0

print(bracket_parser('((()))'))

print(bracket_parser('([{}])'))

print(bracket_parser('(([[{]]}))'))
