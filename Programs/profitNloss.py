from contextlib import suppress


class ProfitLoss(object):
    def __init__(self):
        self.cp = None
        self.sp = None
        self.diff = None
        self.diffPercent = None
        self.mp = None
        self.dis = None
        self.disPercent = None

    def calCP(self):
        if self.cp is None:
            with suppress(TypeError): self.cp = self.sp - self.diff
            with suppress(TypeError): self.cp = (self.sp * 100) // (100 + self.diffPercent)
            with suppress(TypeError): self.cp = self.diff * 100 // self.diffPercent

    def calSP(self):
        if self.sp is None:
            with suppress(TypeError): self.sp = self.diff + self.cp
            with suppress(TypeError): self.sp = self.cp * (100 + self.diffPercent) // 100
            with suppress(TypeError): self.sp = self.mp - self.dis
            with suppress(TypeError): self.sp = self.mp - (self.disPercent * self.mp // 100)

    def calDiff(self):
        if self.diff is None:
            with suppress(TypeError): self.diff = self.sp - self.cp
            with suppress(TypeError): self.diff = self.diffPercent * self.cp // 100

    def calDiffPercent(self):
        if self.diffPercent is None:
            with suppress(TypeError): self.diffPercent = self.diff * 100 // self.cp

    def calMP(self):
        if self.mp is None:
            with suppress(TypeError): self.mp = self.dis * 100 // self.disPercent
            with suppress(TypeError): self.mp = self.dis + self.sp
            with suppress(TypeError): self.mp = (self.sp * 100) // (100 - self.disPercent)

    def calDis(self):
        if self.dis is None:
            with suppress(TypeError): self.dis = self.mp - self.sp
            with suppress(TypeError): self.dis = self.disPercent * self.mp // 100

    def calDisPercent(self):
        if self.disPercent is None:
            with suppress(TypeError): self.disPercent = self.dis * 100 // self.mp
            with suppress(TypeError): self.disPercent = 100 - (self.sp * 100 // self.mp)

    def calAll(self):
        for _ in range(3):
            self.calCP()
            self.calSP()
            self.calDiff()
            self.calDiffPercent()
            self.calMP()
            self.calDis()
            self.calDisPercent()


account = ProfitLoss()

account.cp = 400
account.diffPercent = 80
account.disPercent = 30

account.calAll()
print('cp =', account.cp)
print('sp =', account.sp)
print('diff =', account.diff)
print('diffPercent =', account.diffPercent)
print('mp =', account.mp)
print('dis =', account.dis)
print('disPercent =', account.disPercent)
