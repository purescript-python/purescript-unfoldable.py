def _internalUnfolder(isNothing, fromJust, fst, snd, f, b):
    result = list()
    value = b
    while (True):
        maybe = f(value)
        if( isNothing(maybe) ): return result
        tupleVal = fromJust(maybe)
        result.append( fst(tupleVal) )
        value = snd(tupleVal)

def unfoldrArrayImpl(isNothing):
    return lambda fromJust: lambda fst: lambda snd: lambda f: lambda b: \
        _internalUnfolder(isNothing, fromJust, fst, snd, f, b)
