# 定义装饰器，形参、实参是一个函数对象
# 定义时的参数叫做形参， 传递时的参数叫实参
def func1(xxxx):
    def func2():
        # 这一步代表，传入的函数对象被调用
        xxxx()
        print("我是func2")
    return func2

#TypeError: func1() takes 0 positional arguments but 1 was given
@func1()
def be_decorate():
    print("被装饰器装饰的函数")



# be_decorate()
# 返回传入的be_decorate的函数对象
func1(be_decorate)
# 再加一个() 代表， 调用这个函数对象
