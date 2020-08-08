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


class HouYi(Game):
    """
    后裔，后裔继承了Game的hp 和power。并多了护甲属性。
    重新定义另外一个defense方法：
    final_hp = hp+defense-enemy_power
    enemy_final_hp = enemy_hp - power
    两个hp进行对比，血量先为零的人输掉比赛
    """
    # 如果重名的话，子类的属性，会覆盖掉父类的属性
    def __init__(self, my_hp, your_hp):
        self.defense = 100
        # 继承父类的构造方法，如果父类的构造方法有形参，需要传递参数
        super().__init__(my_hp,your_hp)

    def fight(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.your_power
            self.your_hp = self.your_hp - self.my_power
            print(self.my_hp)
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.your_hp <= 0:
                print("你输了")
                break


houyi = HouYi(1000, 1300)
houyi.fight()





