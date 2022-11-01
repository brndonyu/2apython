
def top(arr):
    return arr[len(arr)-1]

def isoperator(c):
    if c == '+' or c == '-' or c == '*' or c == '^' or c == '/' or c == '//':
        return True

def isempty(arr):
    if len(arr) == 0:
        return True
    else:
        return False

def opprio(op):
    if op == '^':
        return 3
    elif op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    else:
        return -1

def arithmetic(lhs, rhs, op):
    if op == '^':
        return lhs ** rhs
    elif op == '*':
        return lhs * rhs
    elif op == '/':
        quo = lhs / rhs
        if quo.is_integer():
            return int(quo)
        return quo
        
    elif op == '+':
        return lhs + rhs
    elif op == '-':
        return lhs - rhs


def calculate(postfix):
    op_stack = []
    while not isempty(postfix):
        while postfix[0].isnumeric():
            op_stack.append(postfix[0])
            postfix.pop(0)
        rhs = int(op_stack[len(op_stack)-1])
        op_stack.pop(len(op_stack)-1)
        lhs = int(op_stack[len(op_stack)-1])
        op_stack.pop(len(op_stack)-1)
        op_stack.append(arithmetic(lhs, rhs, postfix[0]))
        postfix.pop(0)
    return op_stack[len(op_stack)-1]


def calculator(input):
    input = input.replace('**','^')
    input = input.replace('//','/')
    print(input)
    stackchar = []      #stack to hold numbers
    op_stack = []       #stack to hold operators
    result_queue = []   #result
    for i in input:
        if i.isnumeric():
            result_queue.append(i)
        elif isoperator(i):
            while not isempty(op_stack) and opprio(top(op_stack)) >= opprio(i) and top(op_stack) != '(':
                result_queue.append(top(op_stack))
                op_stack.pop(len(op_stack)-1)
            op_stack.append(i)
        elif i == '(':
            op_stack.append(i)
        elif i == ')':
            while top(op_stack) != "(":
                result_queue.append(top(op_stack))
                op_stack.pop(len(op_stack)-1)
            op_stack.pop(len(op_stack)-1)
    while not isempty(op_stack):
        result_queue.append(top(op_stack))
        op_stack.pop(len(op_stack)-1)
    return calculate(result_queue)
