class Nol:
    def __init__(self, up, down):
        self.up = up
        self.down = down

    @staticmethod
    def div_nol(up, down):
        try:
            return (up / down)
        except:
            return (f"Деление на ноль нельзя")



print(Nol.div_nol(5, 0))
print(Nol.div_nol(5, 10))
