# 定义装饰器，形参、实参是一个函数对象
# 定义时的参数叫做形参， 传递时的参数叫实参
import time


def func1(xxxx):
    def func2():
        print("开始的时间为", time.strftime("%S"))
        # 这一步代表，传入的函数对象被调用
        xxxx()

        print("结束的时间为", time.strftime("%S"))

    return func2

#TypeError: func1() takes 0 positional arguments but 1 was given
@func1
def be_decorate():
    time.sleep(3)
    print("被装饰器装饰的函数")

@func1
def demo2():
    time.sleep(4)
    print("这是一个小demo")


demo2()
# 返回传入的be_decorate的函数对象
# 再加一个() 代表， 调用这个函数对象
