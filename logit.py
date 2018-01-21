from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " была исполнена", end = " ")
        print(*args)
        print()
        return func(*args, **kwargs)
    return with_logging