
# def arithemetic_arranger():
from unittest import result
import re

d = ["32 + 698", "32 + 6984", "3801 - 2"]
y = ["2 + 3", "45 + 43", "23 + 49", "32 + 698",
     "123 + 49", "32 * 6984", "3801 - 2"]
p = list()
# y = y.index()

print(y[0][1])
# if pp[1] != "[+-]":
#     print("Error: Operator must be '+' or '-'.")
print(len(y))
# if len(y) > 5:
#     print('Error: Too many problems.')

# for item in y:
#     items = item.split()
#     len0 = int(len(items[0]))
#     len2 = int(len(items[2]))
#     results = eval(f'{int(items[0])}{items[1]}{int(items[2])}')

# print(results)
# if len0 > len2:
#     length = len0 + 1
# else:
#     length = len2 + 2
# output = f'\n%{length}s\n%s%{length-1}s\n%s' % (
#     items[0], items[1], items[2], '-'*length)

# output = "".join(output)
# p.append(output)
# new_output = f'%6s\n%{length}s' % (output, results)
# print(new_output, end=' ')
# # for xp, ip in enumerate(new_output):
# #     line1 = new_output[xp]
# print(line1, end='')


# * Situations that will return an error:
#   * If there are **too many problems** supplied to the function. The limit is **five**, anything more will return:
# `Error: Too many problems.`

#   * The appropriate operators the function will accept are **addition** and **subtraction**. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
# `Error: Operator must be '+' or '-'.`

#   * Each number (operand) should only contain digits. Otherwise, the function will return:
# `Error: Numbers must only contain digits.`

#   * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
# `Error: Numbers cannot be more than four digits.`


#     * There should be four spaces between each problem.
