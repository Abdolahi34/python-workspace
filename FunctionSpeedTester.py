from time import time

# This is Decorator for measure the Function duration time
def SpeedTester(func):
    def wrapper(*args, **kwargs):
        Start = time()
        func(*args, **kwargs)
        End = time()
        return End - Start
    return wrapper
