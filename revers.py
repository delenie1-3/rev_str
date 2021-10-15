class Reversed:
    def __init__(self):
        pass

    def reversed(self, r_str):#метод смены направления букв
        res = ''
        for i in range(len(r_str)-1, -1, -1):#перебирает строку в обратном напровлении и записываает в res
            res += r_str[i]
        return res

'''#для ручной проверки
revers = Reversed()
n = revers.reversed(input('Введите строку, для реверса: '))
print(n)
'''