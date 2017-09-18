__author__ = 'Surya'
class AveragingDigits:
    def __init__(self, num):
        self.number = num

    def countDigits(self):
        num = self.number
        cnt = 0
        while num > 0:
            cnt += 1
            num = int(num / 10)
        return cnt

    def sumDigits(self):
        num = self.number
        total = 0
        while num > 0:
            total += num % 10
            num = int(num / 10)
        return total

    def averageDigits(self):
        num = self.number
        if num > 0:
            return self.sumDigits()/self.countDigits()
        return 0