class Game():
    def __init__(self, my_hp, your_hp):
        self.my_hp = my_hp
        self.my_power = 200
        self.your_hp = your_hp
        self.your_power = 199

    def fight(self):
        while True:
            self.my_hp = self.my_hp - self.your_power
            self.your_hp = self.your_hp - self.my_power
            print(self.my_hp)
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.your_hp <= 0:
                print("你输了")
                break
    def demo2(self, a, b):
        print(a+b)