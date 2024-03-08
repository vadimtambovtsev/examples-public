def regionals_1992_1993_class_9_task_1():
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


def regionals_1992_1993_class_11_task_24():
    '''
    given: in a country 1993 cities, each city has 93+ roads to other cities. each city is reachable from any city.
    prove: you can reach any city within 62 transfers.

    solution:
    let's prove by counterargument. assume there exists a city with 63+ transfers to get to.
    let's divide the cities into groups, group1 is the departure city, group2 is his connections, etc,
    there will be minimum 1 + 63 + 1 = 65 groups.
    in every three nearby groups, there is 94+ cities
    we round 65 groups up to a number that is divisible by 3, i.e to 66.
    , therefore, there are at least (66/3)*94 = 2068 cities that contradicts the given number of cities.
    '''
    pass


def regionals_1993_1994_class_9_task_27():
    '''
    question: is there any quadratic trinomial P(x) with whole coefficients so that
    for any n that consists only of ones, P(n) will also consist only of ones?

    solution: yes, P(x) = x*(9x+2)
    if n = 1....1, then 9n+2 = 100...001, therefore P(n) = 1...1
    '''
    pass


def regionals_1994_1995_class_10_task_57():
    '''
    given: f(x) = 1/(1-x^3)^(1/3)
    find: f(f(...95times..(f(19))))

    solution:

    if x is not 0 or 1, then
    f(f(x)) = 1/(1-(f(x))^3)^(1/3) = (1-1/x^3)^(1/3)
    f(f(f(x))) = x

    the functions will repeat with cycle 3, therefore 95 mod 3 = 2,
    therefore f(f(...95times..(f(19)))) = f(f(19)) = (1-1/19^3)^(1/3)
    '''
    pass


def regionals_1994_1995_class_10_task_61():
    '''
    given: f(x) = ax2+bx+c, a<b, f(x) >=0 for all x
    find: min((a+b+c)/(b-a))

    solution:
    if f(x) >= 0 for all x, then a > 0, b^2 - 4ac <= 0, therefore c >= b2/4a
    A = (a+b+c)/(b-a),  t = b-a > 0
    A >= (a+b+b2/4a)/(b-a) = (4a2+4ab+b2)/4a(b-a) = (9a2+6at+t2)/4at =
        = 3/2 + (9a2+t2)/4at >= 3/2 + sqrt(9a2t2)/2at = 3/2 + 3/2 = 3
    '''
    pass


def regionals_1996_1997_class_10_task_96():
    '''
    given: a line with 1996 points, equal distance between points.
        Peter colors half of them in red, the other half in blue.
        Then Vasily divides them in pairs (red, blue).

    prove: sum (red,blue) distances does not depend on the way Peter colored the points.

    solution:
        let's prove that the sum will be maximum if the pairs are created this way:
        (leftmost red point, rightmost blue point),etc
        - this allows for maximum overlay of the subintervals, and thus to maximize the sum

        let's evaluate a section k:k+1,
        if k = 998, it is covered with k subintervals
        if k = 997, it is coreded with k - 1 subinvervals etc
        ...
        sum = 1 + 2 + ... 997 + 998 + 997 + ... 1 = 998^2 and does not depend on coloring
    '''
    pass
