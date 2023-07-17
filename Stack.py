class Stack:

    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        """проверка стека на пустоту. Метод возвращает True или False"""
        return not bool(len(self.stack_list))

    def push(self, elem):
        """добавляет новый элемент на вершину стека. Метод ничего не возвращает"""
        self.stack_list.append(elem)

    def pop(self):
        """удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека"""
        return self.stack_list.pop()

    def peek(self):
        """возвращает верхний элемент стека, но не удаляет его. Стек не меняется"""
        return self.stack_list[-1]

    def size(self):
        """возвращает количество элементов в стеке"""
        return len(self.stack_list)
