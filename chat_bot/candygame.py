class CandyGame:
    def __init__(self, candy_num=123, user_name='unknown'):
        import random
        candy_num = 221
        self.candy_num = candy_num
        self.user_name = user_name

    def StartMessage(self):
        return ["continue", f"Начнем с {self.candy_num}"]

    def CandyGameWin(self, num: int, ) -> int: #возвращает лучшее решение или 28
        res = 28
        if num % 29:
            res = num%29
        return res

    def UserTurn(self, num_str: str) -> list:
        try:
            num = int(num_str)
        except:
            return ["continue", "введите число от 0 до 28"]

        if num > 28 or num > self.candy_num:
            return ["continue", "возьмите меньше (до 28)"]
        else:
            self.candy_num -= num
        if self.candy_num == 0:
            return ["\end", f"Вы выиграли!  Поздравляю!"]
        bot_take = self.CandyGameWin(self.candy_num)
        self.candy_num -= bot_take
        if self.candy_num == 0:
            return ["end", f"Я забрал {bot_take}  и выиграл!"]
        else:
            return ["continue", f"Я забрал {bot_take}, осталось {self.candy_num}"]



if '__name__' == '__main__':
    new_game = CandyGame