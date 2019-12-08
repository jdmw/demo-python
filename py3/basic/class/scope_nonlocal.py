var = 'global variable'
def outside():
    var = 'outside variable'
    def inside():
        nonlocal var # = 'inside variable'
        print('inside:var=',var)
    print('outside:var=',var)
    inside()
outside()
print('global:var=',var)