"这是一个演示模块"

print("模块级别语句")
def foo():
    print("模块级别函数")
foo()

if __name__ == "__main__":
    print("这是最小的空模块")