import operator
OPERATORS = {'+': (1, operator.add), '-': (1, operator.sub),
             '*': (2, operator.mul), '/': (2, operator.truediv)}


def validate(line):
    for i in line:
        if i not in '1234567890.()+-*/ ':
            raise IndexError


def parse(line):
    num = ''
    for i in line:
        if i in '1234567890.':
            num += i
        elif num:
            yield float(num)
            num = ''
        if i in OPERATORS or i in '()':
            yield i
    if num:
        yield float(num)


def sort(parsed):
    tmp = []
    for i in parsed:
        if i in OPERATORS:
            while tmp and tmp[-1] != '(' and OPERATORS[i][0] <= OPERATORS[tmp[-1]][0]:
                yield tmp.pop()
            tmp.append(i)
        elif i == ')':
            while tmp:
                x = tmp.pop()
                if x == '(':
                    break
                yield x
        elif i == '(':
            tmp.append(i)
        else:
            yield i
    while tmp:
        yield tmp.pop()


def calc(string_sort):
    tmp = []
    for i in string_sort:
        if i in OPERATORS:
            y = tmp.pop()
            x = tmp.pop()
            tmp.append(OPERATORS[i][1](x, y))
        else:
            tmp.append(i)
    return tmp[0]


if __name__ == '__main__':
    inp = input()
    try:
        validate(inp)
        print(calc(sort(parse(inp))))
    except ZeroDivisionError:
        print("You can't divide by 0! Enter an expression that doesn't contain division by 0")
    except IndexError:
        print("Invalid mathematical expression! The expression must contain only numbers 0-9, " +
              "brackets and arithmetic operations")





