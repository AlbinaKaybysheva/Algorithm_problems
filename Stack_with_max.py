# Стек с поддержкой максимума
# Реализовать стек с поддержкой операций push, pop и max.
# Вход: Последовательность запросов push, pop и max .
# Выход: Для каждого запроса max вывести максимальное
# число, находящееся на стеке.

class Stack(object):
    def __init__(self):
        self.stack = []
        self.max_list = []
        self.max = max

    def Push(self, item):
        self.stack.append(item)
        if len(self.max_list) == 0:
            self.max_list.append(item)
        else:
            if item > self.max_list[len(self.stack) - 2]:
                self.max_list.append(item)
            else:
                self.max_list.append(self.max_list[len(self.stack) - 2])
        return self.stack

    def Pop(self):
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()
            self.max_list.pop()
        return self.stack

    def Max(self):
        return self.max_list[len(self.max_list) - 1]

def Request(stack, s):
    if s.startswith('push'):
        num = int(s[s.index(' ') + 1:])
        return stack.Push(num)
    elif s.startswith('pop'):
        return stack.Pop()
    elif s.startswith('max'):
        print(stack.Max())

def main():
    n = int(input())
    my_stack = Stack()
    for i in range(n):
        Request(my_stack, input())

if __name__ == '__main__':
    main()