def addnum(a,b,method='add'):
    if method=='add':
       # b=str(b)
        c=a+b
        print(c)
    elif method=='sub':
        c=a-b
        print(c)
    elif method=='mul':
        c=a*b
        print(c)
    elif method=='div':
        c=a/b
        print(c)

def add(x,y):
    addnum(x,y)
def sub(x,y):
    addnum(x,y,method='sub')
def mul(x,y):
    addnum(x,y,method='mul')
def div(x,y):
    addnum(x,y,method='div')