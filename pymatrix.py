def getTranspose(a):
    return [[a[i][j] if i==j else a[j][i]
            for j in range(len(a[i]))]
            for i in range(len(a))]

def getMinor(a,i,j):
    return [r[:j]+r[j+1:] for r in (a[:i]+a[i+1:])]

def getDeterminant(a):
    #Summed a list instead of keeping a running total cause one-liners are life
    return float(a[0][0]*a[1][1] - a[0][1]*a[1][0]) if len(a) == 2 else\
        sum([(-1 if j%2 else 1)*a[0][j]*getDeterminant(getMinor(a,0,j))
        for j in range(len(a))])

def getInverse(a):
    #The only two line function cause I couldn't justify recalculating the
    #determinant a stupid number of times. Sad.
    d = getDeterminant(a)
    return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]] if len(a) == 2 else\
        getTranspose(
            [[(-1 if (i+j)%2 else 1)*getDeterminant(getMinor(a,i,j))/d
            for j in range(len(a))]
            for i in range(len(a))])

def getProduct(a,b):
    return [[sum([x*y for x,y in zip(a[i],[b[k][j] for k in range(len(b))])])
        for j in range(len(b[0]))]
        for i in range(len(a))]

def getScalarMult(a,s):
    return [[a[i][j]*s for j in range(len(a[0]))] for i in range(len(a))]
