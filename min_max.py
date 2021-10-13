# YouView basic Online Test
def min_max(l):
    '''
    Return min and max from a list of values
    '''
    min,max=None,None
    for item in l:
        if min==None:
            min=item
        else:
            if min>=item:
                min=item
        if max==None:
            max=item
        else:
            if max<=item:
                max=item
    return min,max

if __name__ == "__main__":
    l = []
    assert min_max(l) == (None,None)

    l = [-10,0,1,2,3,3,4,4]
    assert min_max(l) == (-10,4)

    l = range(-99,1000)
    assert min_max(l)==(-99,999)
    
    print("min_max output",min_max(l))
    print("Testing OK")
    
