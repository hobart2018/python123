def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:]) + s[0]

def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)