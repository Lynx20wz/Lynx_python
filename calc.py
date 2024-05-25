import operator
import re
def calc3(a, b, op1, op2, c):
    return op2(c, int(op1(a, b)))
def calc2(a, b, op1):
    return op1(a, b)

operator_slov = {
    '+': operator.add,
    'плюс': operator.add,
    '-': operator.sub,
    'минус': operator.sub,
    '*': operator.mul,
    'умножить': operator.mul,
    '/': operator.truediv,
    'делить': operator.truediv
}
while True:
    a = int(input("Первое число: "))
    op1_str = input("Первое действия: ",)
    b = int(input("Второе число: "))
    op2_str = input("Второе действия: ")
    if op2_str == '=':
        op1 = operator_slov.get(op1_str, None)
        print("Ответ:", calc2(a, b, op1))
    else:
        c = int(input("Третье число: "))
        op1 = operator_slov.get(op1_str, None)
        op2 = operator_slov.get(op2_str, None)

        print("Ответ:", calc3(a, b, op1, op2, c))

