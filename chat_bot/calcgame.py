class CalcGame():
    def __init__(self, user_name='1'):
        self.user_name = user_name
        self.inner_expression = []


    def CalcList(self) -> str:
        expressions = ['/', '*', '+', '-']
        for expr in expressions:
            while self.inner_expression.count(expr) != 0:
                i = self.inner_expression.index(expr)
                a = self.inner_expression.pop(i - 1)
                x = self.inner_expression.pop(i - 1)
                b = self.inner_expression.pop(i - 1)
                self.inner_expression.insert(i - 1, self.CalcTwo(a, x, b))
        return self.inner_expression[0]


    def UserTurn(self, equation='( 2 + 4 ) / 3'):

        self.expr_list = equation.split()
        try:
            left_hook = 0
            right_hook = 0
            self.inner_expression = []
            while self.expr_list.count('(') != 0:
                self.inner_expression = []
                right_hook = self.expr_list.index(')')
                self.expr_list.pop(right_hook)
                for i in range(right_hook - 1, -1, -1):
                    elem = self.expr_list.pop(i)
                    if elem == '(':
                        left_hook = i
                        break
                    else:
                        self.inner_expression.insert(0, elem)
                self.expr_list.insert(left_hook, self.CalcList())
            self.inner_expression = self.expr_list
            return ["\end",  f"Выражение {equation}\n = {self.CalcList()}"]
        except:
            return ["\continue", f"Выражение {equation} содержит ошибку"]


    def CalcTwo(self, a: str, x: str, b: str):
        """ вычисляет простое выражение """
        if x == '/':
            return str(float(a) / float(b))
        if x == '*':
            return str(float(a) * float(b))
        if x == '+':
            return str(float(a) + float(b))
        if x == '-':
            return str(float(a) - float(b))


if '__name__' == '__main__':
    s =str ( ( 3 + ( 1 + 4 ) ) * ( 8 + 1 + 2 ) - ( 3 + 6 * 2 / 3 ) )
    new_expression = CalcGame()
    print(new_expression.UserTurn(equation=s))