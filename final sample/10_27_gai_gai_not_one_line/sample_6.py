'''
is_valid_prefix_expression(expression) checks whether the string expression
represents a correct infix expression (where arguments follow operators).

evaluate_prefix_expression(expression) returns the result of evaluating expression.

For expression to be syntactically correct:
- arguments have to represent integers, that is, tokens that can be converted to an integer
  thanks to int();
- operators have to be any of +, -, * and /;
- at least one space has to separate two consecutive tokens.

Assume that evaluate_prefix_expression() is only called on syntactically correct expressions,
and that / (true division) is applied to a denominator that is not 0.

You might find the reversed() function, the split() string method,
and the pop() and append() list methods useful.
'''

from operator import add, sub, mul, truediv


class ListNonEmpty(Exception):
    pass


def is_valid_prefix_expression(expression):
    '''
    >>> is_valid_prefix_expression('12')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ 12 4')
    Correct prefix expression
    >>> is_valid_prefix_expression('- + 12 4 10')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ - + 12 4 10 * 11 4')
    Correct prefix expression
    >>> is_valid_prefix_expression('/ + - + 12 4 10 * 11 4 5')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ / + - + 12 4 10 * 11 4 5 - 80 82 ')
    Correct prefix expression
    >>> is_valid_prefix_expression('twelve')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('2 3')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ + 2 3')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ / 1 2 *3 4')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ +1 2')
    Correct prefix expression
    >>> is_valid_prefix_expression('++1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ +1 -2')
    Correct prefix expression
    '''
    stack = []
    operator = ['+','-','*','/']
    try:
        expres = expression.split()         #  delete space 
        for i in expres:
            if i in operator or int(i):
                stack.append(i)
            # approach 1
            while len(stack) >= 3 and stack[-1] not in operator and stack[-2] not in operator and stack[-3] in operator:
                right = stack.pop()
                left = stack.pop()
                op =stack.pop()
                # print(left + op + right)
                result = eval(left+ op + right)
                stack.append(str(result))
                # print(stack) 
            # approach 2  
            # while len(stack) >= 3 and stack[-1] not in operator and stack[-2] not in operator:
            #     stack = stack[:-3] + ['1']
        # print(stack)
        if len(stack) > 1:
            raise ListNonEmpty
        if len(stack) == 1 and stack[0] in operator:
            raise ListNonEmpty
        # Replace pass above with your code
    # - IndexError is raised in particular when trying to pop from an empty list
    # - ValueError is raised in particular when trying to convert to an int
    #   a string that cannot be converted to an int
    # - ListNonEmpty is expected to be raised when a list is found out not to be empty
    except (IndexError, ValueError, ListNonEmpty, ZeroDivisionError):
        print('Incorrect prefix expression')
    else:
        print('Correct prefix expression')
# is_valid_prefix_expression('+ - + 12 4 10 * 11 4')
# is_valid_prefix_expression('- + 12 4 10') 
    
def evaluate_prefix_expression(expression):
    '''
    >>> evaluate_prefix_expression('12')
    12
    >>> evaluate_prefix_expression('+ 12 4')
    16
    >>> evaluate_prefix_expression('- + 12 4 10')
    6
    >>> evaluate_prefix_expression('+ - + 12 4 10 * 11 4')
    50
    >>> evaluate_prefix_expression('/ + - + 12 4 10 * 11 4 5')
    10.0
    >>> evaluate_prefix_expression('+ / + - + 12 4 10 * 11 4 5 - 80 82 ')
    8.0
    >>> evaluate_prefix_expression('+ +1 2')
    3
    >>> evaluate_prefix_expression('+ +1 -2')
    -1
    '''
    # Insert your code here

    expre = expression.split()
    stack = []
    operator = ['+','-','*','/']
    # num = 1
    for i in expre:
        stack.append(i)
        while len(stack) >= 3 and stack[-1] not in operator and stack[-2] not in operator:
            value = eval((stack[-2]) + stack[-3] + (stack[-1]))
            stack = stack[:-3] + [str(value)]
    # return int(stack[0]) if '.' not in stack[0] else float(stack[0])
    if '.' in stack[0]:
        return float(stack[0])
    else:
        return int(stack[0])


#    return int(stack[0])
# print(evaluate_prefix_expression('+ - + 12 4 10 * 11 4'))
# evaluate_prefix_expression('+ +1 -2')                      
# print(evaluate_prefix_expression('+ / + - + 12 4 10 * 11 4 5 - 80 82 '))

# print('###############')
if __name__ == '__main__':
    import doctest
    doctest.testmod()   
