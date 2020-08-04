"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

def game():
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 199
    my_final_hp = my_hp - your_power
    enemy_final_hp = your_hp - my_power
    # 三目运算等同于下面的if-else，只是语法更简洁
    # print("我赢了") if my_final_hp > enemy_final_hp else print("你赢了")
    # 判断条件 if 执行结果1 else 执行结果2
    # if 判断条件:
    #     执行结果1
    # else:
    #     执行结果2
    # 快捷键： ctrl +d  复制当前行到下一行
    # 快捷键： ctrl+/ 复制当前行到下一行
    if my_final_hp > enemy_final_hp:
        print("我赢了")
    else:
        print("你赢了")

game()