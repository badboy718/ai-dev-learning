def fn1(fn):
    print("fn1")
    def fn2(num1, num2):
        print("fn2", num1, num2)
        res=fn(num1, num2)
        print(res)
    return fn2

@fn1
def fn3(n1,n2):
    print("fn3")
    return n1+n2

@fn1
def fn4(n1,n2):
    print("fn4")
    return n1+n2

fn3(10,20)
fn4(50,100)