import functools
from datetime import datetime, timedelta

def do_log(func,*args,**kw):
    print("execute {}{}".format(func.__name__, args or (str(kw).replace("{", "(").replace("}", ")"))))

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        do_log(func,*args,**kw)
        return func(*args,**kw)
    return wrapper

@log
def current_time():
    print(datetime.now())


def checkPositive(func):
    # set: wrapper.__name__ = func.__name__
    @functools.wraps(func)
    def wrapper(*args,**kw):
        if(func.__name__ == "take_fruits"):
            num = args[0] if args else kw['num']
            if num <= 0 :
                print("can't take %d fruits" % num)
                return False
        return func(*args,**kw)
    return wrapper


@checkPositive
@log
def take_fruits(num):
    print("take %d fruits" % num)
    return True


def catch_exception(msg_header="error"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            do_log(func,*args,**kw)
            try:
                return func(*args, **kw)
            except Exception as e :
                print("{}---{}".format(msg_header, e))
                return
        return wrapper
    return decorator

@catch_exception("div error")
def div(a,b):
    return a / b

if __name__ == "__main__":
    current_time()
    take_fruits(1)
    print(take_fruits(num=-1))
    print(current_time)
    print(take_fruits)
    print(div(1,0))
    print(div(1,1))
