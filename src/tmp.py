def f(a, arg2, arg3):
    return "F:{0} {1} {2}".format(a, arg2, arg3)

def g(a, arg1):
    return "G: {0} {1}".format(a, arg1)

def h(a):
    return "H: {0}".format(a)

result = f(
    g(
        h('df'), arg1=1
    ),
    arg2=2, arg3=3)

print result
