"""
        postfix_evaluation is a class which will accept a postfix expression and retuns the evaluated result
        for example
        i have the expression : 23+4-
        then this will return 1
        which is (2+3)-4

        POSTFIX_EVALUATION limits upto single digit evaluation
"""
class postfix_evaluation():
    def __init__(self, exp):
        self.expression = exp  # expression in local variable
        self.__stk = [] # declared an empty stack
        self.__operation = ["/", "*", "+", "-", "%"] # a list of operations which will be performed
        pass
    def evaluate(self):

        for x in self.expression:
            if x not in self.__operation:
                self.__stk.append(x)
            else:
                calc = self.__compute(x) # getting result
                self.__stk.append(calc) # pushing back to the stack
            pass
        return self.__stk[0] # at last the first value of stack will be our evaluated result

    # private method to compute the result
    def __compute(self, opr):
        # poping the number
        b = int(self.__stk.pop())
        a = int(self.__stk.pop())

        # appylying the operation and returning the value
        if opr == "*":
            return a*b
        elif opr == "-":
            return a-b
        elif opr == "+":
            return a+b
        elif opr == "/":
            return a//b  # this will do integer division
        elif opr == "%":
            return a%b

        pass
    pass
