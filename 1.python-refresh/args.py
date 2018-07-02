def func(arg1, arg2):
    return arg1 + arg2


def func2(*args):
    return sum(args)


func2(1, 4, 2, 6)


def whats_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


# positional arguments should follow the named arguments
whats_kwargs(1, 2, 3, 4, foo=5, bar=6)
# (1, 2, 3, 4)
# {'foo': 5, 'bar': 6}


def methodception(another):
    return another()


def add():
    return 4 + 3


addtion = methodception(add)
print(addtion)

print(methodception(lambda: 40 + 30))

my_list = [13, 40, 20, 17, 43]
even_list = list(filter(lambda x: x % 2 == 0, my_list))  # filter
print(even_list)

even_list2 = [x for x in my_list if x % 2 == 0]  # list comparehension
print(even_list2)
