def regionals_class_9_task_1():
    '''
    given: a,b in R.
    prove: a*a +a*b + b*b >= 3*(a + b - 1)

    solution:
    f(x) = a*a +a*b + b*b - 3*(a + b - 1) = a*a + (b-3)*a + (b*b - 3*b + 3)
    discriminant(f) = -3 * (b-1) * (b-1) <= 0

    (discriminant <= 0) && (coefficient in front of a*a in f(x) = 1 > 0) => f(x) >= 0 for all (a,b)
    f(x) = 0 if (a=1, b=1)
    '''
    pass

