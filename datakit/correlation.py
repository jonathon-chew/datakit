import math 

def correlation(x: list[int], y: list[int]) -> float:

    """
    ∑xy = 12258
    ∑x = 151
    ∑y = 336
    ∑x² = 5625
    ∑y² 28724
    n = 4

    Put all the values in the Pearson's correlation coefficient formula:
    R= frac{n(∑xy) - (∑x)(∑y)}{sqrt{[n∑x²-(∑x)²][n∑y²-(∑y)²}}             
    R = 4(12258) - (151)(336) / √[4(5625)-(151)²][4(28724)-(336)²]       
    """

    if len(x) != len(y):
        raise ValueError("[ERROR]: x and y are not the same length")
    
    if len(x) == 0:
        raise ValueError("[ERROR]: x is empty")

    if len(y) == 0:
        raise ValueError("[ERROR]: y is empty")

    n = len(x)
    xSum = sum(x)
    ySum = sum(y)
    xSquared = sum([x2**2 for x2 in x])
    ySquared = sum([y2**2 for y2 in y])
    xTimesy = sum([ x[num] * y[num] for num in range(n)])

    R = (
            (
                n * xTimesy
            ) - (
                (xSum * ySum)
            )
        ) / math.sqrt(
            (
                (n*xSquared) - (xSum ** 2)
            ) * (
                (n*ySquared) - ((ySum) ** 2)
            )
        )

    return R

x = [40, 25, 22, 54]
y = [99, 79, 69, 89]

print(correlation(x, y))