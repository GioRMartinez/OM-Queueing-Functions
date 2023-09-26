import math
def is_valid(lamda, mu, c=1):
    """
    This is a boolean function that takes lambda, mu, c, and checks if all variables are greater than zero

    Parameters:
        lamda: Arrival Rate
        mu: Service Rate
        c: Number of Servers

    Returns:
         True or False
    """
    # Confirming if lamda is an interger or tuple/list
    if type(lamda) == int:

        # Checks if the parameters are greater than zero
        if lamda < 0 or mu < 0 or c < 0:
            return False
        else:
            return True

    # If lamda is a tuple/list then we calculate an aggargate lamda
    else:
        for lamda in lamda:
            if lamda < 0 or mu < 0 or c < 0:
                r = False
                break
            else:
                r = True
        return r

def is_feasible(lamda, mu, c=1):
    """
    This is a boolean function that takes lambda, mu, c, and checks if the calculations of ro are greater than one.

    Parameters:
        lamda: Arrival Rate
        mu: Service Rate
        c: Number of Servers

    Returns:
         True or False
    """
    # Checking if the paramaters are greater than zero
    if is_valid(lamda, mu, c) == True:

        # Checking if lamda is an int or tuple/list to use correct formula
        if type(lamda) == int:
            ro = lamda/(c*mu)
        else:
            ro = sum(lamda)/(c*mu)
    else:
        return math.nan

    # Checking if ro is greater than one
    if ro < 1:
        return True
    else:
        return False

def calc_p0(lamda, mu, c=1):
    """
    This is a function that takes lambda, mu, c, and calculates the probability the Queue is empty

    Parameters:
        lamda: Arrival Rate
        mu: Service Rate
        c: Number of Servers

    Returns:
         p0 - for vaild, feasible queues
         math.nan - Function is invalid
         math.inf - function is infeasible
    """

    # Checking if the variables are valid
    if is_valid(lamda, mu, c) == True:

        # Checking if the variables are feasible
        if is_feasible(lamda, mu, c) == True:

            # Checks if the lamda is an integer or a tuple/list to use correct ro and r formulas
            if type(lamda) == int:
                ro = lamda / (c * mu)
                r = lamda / mu
            else:
                lamda = sum(lamda)
                ro = lamda / (c * mu)
                r = lamda / mu

            # Checks if c is greater than one to use correct p0 formula
            if c == 1:
                p0 = 1 - ro
                return p0
            else:
                n = 0
                for i in range(c):
                    x = ((r ** i) / (math.factorial(i)))
                    n += x
                n += (r ** c) / (math.factorial(c) * (1 - ro))
                p0 = 1 / n
                return p0

        # If not feasible return math.inf
        else:
            return math.inf
    # if not valid return math.nan
    else:
        return math.nan


def calc_lq_mmc(lamda, mu, c=1):
    """
    This is a boolean function that takes lambda, mu, c, and calculates the average number of customer in the queue

    Parameters:
        lamda: Arrival Rate
        mu: Service Rate
        c: Number of Servers

    Returns:
         lq - valid, feasible queues
         math.nan - Function is invalid
         math.inf - function is infeasible
    """

    # Checking if the variables are valid
    if is_valid(lamda, mu, c) == True:

        # Checking if the variables are feasible
        if is_feasible(lamda, mu, c) == True:
            if type(lamda) == int:
                ro = lamda / (c * mu)
                r = lamda / mu
            else:
                lamda = sum(lamda)
                ro = lamda / (c * mu)
                r = lamda / mu

            # Checks if c is greater than one to use correct lq formula
            if c == 1:
                lq = (lamda ** 2) / (mu * (mu * lamda))
                return lq
            else:
                q = calc_p0(lamda, mu, c)
                lq = (((r ** c) * ro) / (math.factorial(c) * ((1 - ro) ** 2))) * q
                return lq
        # If infeasible, returns math.inf
        else:
            return math.inf
    # If invalid, returns math.nan
    else:
        return math.nan
