class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        if len(self.values) == 0:
            return True
        else:
            return False
    
    def push(self, value):
        self.values.append(value)
    
    def pop(self):
        if not self.is_empty():
            a = self.values[:-1]
            self.values = a
            return a
        else:
            raise IndexError("Nothing in stack")


def infix_to_suffix(vyraz):

    stak = Stack()
    output = []

    nums = '1234567890'
    
    operators = {'+':1,'-':1,'*':2,'/':2}

    for part in vyraz:
        if part in nums:
            output.append(part)
        elif part == '(':
            stak.push('(')
        elif part == ')':
            while stak.values[-1] != '(':
                if stak.values[-1] in operators:
                    output.append(stak.values[-1])
                stak.pop()
            stak.pop()
        elif part in operators:
            if operators[part] >1:
                for j in stak.values[::-1]:
                    if j in ['(', ')']:
                        break
                    elif operators[j] >1:
                        stak.pop()
                        output.append(j)
            else:
                for j in stak.values[::-1]:
                    if j in ['(', ')']:
                        break
                    elif j in operators:
                        stak.pop()
                        output.append(j)
            stak.push(part)

    temp = [i for i in stak.values]

    for i in temp:
        if i in operators:
            stak.pop()
            output.append(i)
    
    return output


def calculate_exp(expe):

    operand_stack = Stack()

    nums = '0123456789'

    operators = ['+', '-', '*', '/']

    for part in expe:
        if part in nums:
            operand_stack.push(int(part))
        if part in operators:
            a = operand_stack.values[-1]
            operand_stack.pop()
            b = operand_stack.values[-1]
            operand_stack.pop()
            match part:
                case '+':
                    result = b + a
                case '-':
                    result = b - a
                case '*':
                    result = b * a
                case '/':
                    result = b / a
            operand_stack.push(result)
    return result


exp = "((2+3)-4*(5/6))+7"
suffix_exp = infix_to_suffix(exp)
print(''.join(suffix_exp))

calculated = calculate_exp(suffix_exp)
print(calculated)

