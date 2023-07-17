from Stack import Stack


def is_balanced(string):
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    stack = Stack()
    for char in string:
        if char in brackets.values() and stack.is_empty():
            return False
        elif char in brackets:
            stack.push(char)
        elif char != brackets[stack.pop()]:
            return False
    if stack.is_empty():
        return True
    else:
        return False



string = input('Введите строку, в которой необходимо проверить сбалансированность скобок:\n')
result = ("Несбалансированно", "Сбалансированно")[is_balanced(string)]
print(result)


assert is_balanced("(((([{}]))))") is True
assert is_balanced("[([])((([[[]]])))]{()}") is True
assert is_balanced("{{[()]}}") is True
assert is_balanced("}{}") is False
assert is_balanced("{{[(])]}}") is False
assert is_balanced("[[{())}]") is False
