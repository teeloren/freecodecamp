import re

# def arithemetic_arranger():
d = ["2 + 3", "45 + 43", "23 + 49"]
d2 = ["32 + 698", "123 + 49"]
d3 = ["32 + 6984", "3801 - 2"]
for item in d:
    # items = re.split('[+-]', item)
    items = item.split()
    length = 1
    len0 = int(len(items[0]))
    len2 = int(len(items[2]))
    # print(len0)
    # print(len2)
    if (len0 and len2) < 3:
        length = length + 1
        output = '{:>4}\n{} {}\n{}'.format(
            items[0], items[1], items[2], '-'*length)
        print(output)

    if len0 >= len2:
        length = len0+1
        output = '{:>4}\n{} {}\n{}'.format(
            items[0], items[1], items[2], '-'*length)
    elif len0 < len2:
        length = len2+2
        output = '{:>5}\n{} {}\n{}'.format(
            items[0], items[1], items[2], '-'*length)

    # # if length <= 3:
    # # length = length+1
    # # else:
    # # length = length

    # # if '+' in item:
    # #     output = '{:>6}\n{:<}\n{}'.format(items[0],
    # #                                        items[1], '-'*length)
    # # else:
    # #     output = '{:>}\n-{}\n{}'.format(items[0], items[1], '-'*length)
    # print(output)
    # print(output, end='')
    # print(output,end='', flush=True)
