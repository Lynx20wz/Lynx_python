# def get_first_matching_object(predicate, objects=None):
#     if objects is None: objects = []
#     for obj in objects:
#         if object := predicate(obj):
#             return object
#     return None
#
#
# print(get_first_matching_object(lambda x: x==1, [1, 2, 3, 4]))

class stack:
    def __init__(self, numbers: list = None):
        if numbers is None: numbers = []
        self.stack = numbers
        self.min_number = 0
        if self.stack == []:
            self.min_num()

    def min_num(self):
        if self.stack == []:
            self.min_number = 0
        else:
            y = self.stack[0]
            for i in range(len(self.stack)):
                x = self.stack[i]
                if x <= y:
                    self.min_number = x
                    y = x
        return self.min_number

    def push(self, num: int):
        self.stack.append(num)
        if num < self.min_number or self.min_num is []:
            self.min_number = num
        return f'Было добавлено значение: {self.stack[-1]}'

    def pop(self):
        delete_num = self.stack.pop()
        if delete_num == self.min_number:
            self.min_num()
        return f'Было удалено: {delete_num}'


    def top(self):
        if self.min_number is not []:
            return f'В списке нет значений'
        else:
            return f'Последнее добавленное значение {self.stack[-1]}'

    def get_min(self):
        self.min_num()
        return f'Минимальное значение: {self.min_number}'


list_of_number = stack([2, 7, 4])
#tests
print(list_of_number.get_min())
print(list_of_number.push(1))
print(list_of_number.get_min())
print(list_of_number.pop())
print(list_of_number.get_min())
print(list_of_number.top())
print(*list_of_number.stack, sep=', ')
