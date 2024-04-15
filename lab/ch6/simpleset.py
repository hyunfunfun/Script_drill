from functools import *

def intersect(*ar): #가변인자 튜플
    return reduce(__intersectSC,ar)

def __intersectSC(listX,listY):
    setList=[]
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList

def difference(*ar):#difference('abc','cde')->ar=('abc','cde')
    setList=[]
    intersectSet = intersect(*ar)
    unionSet = union(*ar)
    for x in unionSet:
        if not x in intersectSet:
            setList.append(x)
    return setList

def union(*ar):
    setList=[]
    for item in ar: #ar=('abc','cde')
        for x in item: #item = 'abc','cde'
            if not x in setList:
                setList.append(x)
    return setList