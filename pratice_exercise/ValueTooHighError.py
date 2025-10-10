class ValueTooHighError(Exception):
    def __init__(self,x):
        self.x = x
def higherthan100(x):
    try:
        if x > 100:
            raise ValueTooHighError(x)
    except KeyError:
        print("another error")
try:
    higherthan100(700)
    print("normal")
except ValueTooHighError:
    print("number higher than 100")