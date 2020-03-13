def _internalUnfolder(isNothing, fromJust, fst, snd, f, b):
    result = list()
    value = b
    while (true):
        maybe = f(value)
        if( isNothing(maybe) ): return result
        tupleVal = fromJust(maybe)
        result.push( fst(tupleVal) )

def unfoldrArrayImpl(isNothing):
    lambda fromJust: lambda fst: lambda snd: lambda f: lambda b: \
        _internalUnfolder(isNothing, fromJust, fst, snd, f, b)
