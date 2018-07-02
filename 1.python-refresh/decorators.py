import functools


# ====== simple decorators ======
def my_decorator(func):
    @functools.wraps(func)  # keep the name and doc strings for func
    def func_that_runs_func(*args):
        print("inside the decorator ")
        func(*args)
        print("after the function call")
    return func_that_runs_func


@my_decorator
def my_func(name):
    print("Hello " + name)


my_func("John")

# ====== decorator with arguments ======
# such as @dec(56)


def decorator_with_args(num):
    def my_decorator(func):
        @functools.wraps(func)
        def func_that_runs_func(*args, **kwargs):
            # any logic can be put here
            print(f"inside the decorator, number is {num}")
            func(*args, **kwargs)
            print("after the function call")
        return func_that_runs_func
    return my_decorator


@decorator_with_args(80)
def my_func2():
    print("Hello world")


my_func2()

# another example


def access_control_decorator(allowed_usertype):
    def my_decorator(func):
        @functools.wraps(func)
        def ori_func(user_name, user_type):
            if user_type == allowed_usertype:
                print("admin user")
                func(user_name, user_type)
            else:
                print(f"user type: {user_type}")
                print("redirect to home page")
        return ori_func
    return my_decorator


@access_control_decorator("Admin")
def render_admin_page(username, user_type):
    print(f"welcome to the admin page {username}")


render_admin_page("Jasen", "Admin")
