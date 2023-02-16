def dec(fn):
    def wrapper(a,b):
        if a>b:
            return fn(a,b)
        else:
            return fn(b,a)
    return wrapper


@dec
def sub(a,b):
    return a-b

@dec
def div(a,b):
    return a/b

print(sub(10,20))
print(div(10,20))