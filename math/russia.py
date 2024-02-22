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


def regionals_1992_1993_class_11_task_8():
    '''
    given: in a country 1993 cities, each city has 93+ roads to other cities. each city is reachable from any city.
    prove: you can reach any city within 62 roads.

    solution:
    let's prove by counterargument. assume there exists a city with 63+ roads to get to.
    let's divide the cities into groups, group1 is the departure city, group2 is his connections, etc,
    there will be minimum 1 + 63 + 1 = 65 groups.
    in every group there is at least 93+1 = 94 cities.
    in every three nearby groups, there is 94+ cities
    we round 65 groups up to a number that is divisible by 3, i.e to 66.
    , therefore, there are at least (66/3)*94 = 2068 cities that contradicts the given number of cities.
    '''
    pass