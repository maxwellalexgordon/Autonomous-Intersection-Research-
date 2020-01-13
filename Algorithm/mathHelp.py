import cmath
# helper functions
def expect(c, b, a):
    if (a == 0):
        a = 0.0000002
    a = a / 2.0
    d = (b ** 2) - (4.0 * a * c)
    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2.0 * a)
    sol2 = round(abs(((-b + cmath.sqrt(d)) / (2.0 * a))), 3)
    #print('The solution are {0} and {1}'.format(sol1, sol2.__abs__()))
    return sol2.__abs__()