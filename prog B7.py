import math
try:
    print("try block")
    x=int(input("enter the value of x: "))
    y=int(input("enter the value of y: "))
    if y>x:
        z=y/x
        raise TypeError
    else:
        z=x/y
        e=math.exp(y)
except IndexError:
    print("--IndexError exception--")
except TypeError:
    print("typeerror exception")
    print("invalid operation")
except ValueError:
    print("valueerror exception")
    print("invalid literal for int()with base 10")
except ZeroDivisionError:
    print("zerodivisionerror exception")
    print("division by zero not accepted")
except OverflowError as oe:
    print("after overflow",oe)
else:
    print("else block reached")
    print("division= ",z)
    print("exponents= ",e)
finally:
    print("finally block reached")
x=0
y=0
print("out of try,except,else and finally blocks.")
