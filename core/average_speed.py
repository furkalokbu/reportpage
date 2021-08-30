
class AverageSpeed():

    """Return the speed for normal data 
    >>> res = AverageSpeed()
    >>> values = [[3.0,10],[6.0,2],[10.0,10]]
    >>> res.speed(values)
    [0.3, 3.0, 1.0]

    Return speed for zero and value less than zero:
    >>> values = [[3.0,0],[6.0,-1]]
    >>> res.speed(values)
    []
    >>> values = [0.3, 3.0, 1.0]
    >>> round(res.average_speed(values),6)
    1.433333
    >>> values = []
    >>> res.average_speed(values)
    0
    """

    def speed(self, values):

        velocities = []
        for pos, time in values:
            if time > 0:
                velocity = float(pos/time)
                velocities.append(velocity)
            else:
                continue
        return velocities

    def average_speed(self, values):

        from numpy import mean
        if values:
            return mean(values)
        return 0



if __name__ == "__main__":
    import doctest
    doctest.testmod()
