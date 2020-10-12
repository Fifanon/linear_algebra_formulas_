import math

##compute the ratio of the series
def seriesRatio(x,i):
    r = -(x**2)/((i+2)*(i+1))

    return r
def enterValues():
    try:
        x = float(input("Enter value of x: "))
    except ValueError:
        print("Enter a number")
    try:
        n = int(input("Enter number of terms in series: "))
    except ValueError:
        print("Enter a number")
    return x, n
#Compute cosine of x using the infine series approximation 
def cosInfiniteSeries():
    print("***** Cosine series ****")
    cosx = 1
    term  = 1
    x, n = enterValues()

    for i in range (0, n, 2):
        ratio = seriesRatio(x,i)
        term = term * ratio
        cosx = cosx + term
    ##printing math.cos generated cosine value for x, to compare with the only ouput
    ##by out function
    print("\ncos (",int(x),"): ", cosx)
    print("math.cos of",int(x), ": ", math.cos(x))
    return


def sineInfiniteSeries():
    print("***** Sine series ****\n")
    x, n = enterValues()
    term = x
    sinx = term

    for i in range (1, n, 2):
        ratio = seriesRatio(x,i)
        term = term * ratio
        sinx = sinx + term
    ##printing math.cos generated cosine value for x, to compare with the only ouput
    ##by out function
    print("\ncos (",int(x),"): ", sinx)
    print("math.sin of",int(x), ": ", math.sin(x))
    return
##calling our cosine and sine series functions 
sineInfiniteSeries()
sineInfiniteSeries()
