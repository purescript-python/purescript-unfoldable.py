def _internalUnfolder (isNothing, fromJust, fst, snd, f, b):
    result = []
    value = b;
    while (true):
        tupleVal = f(value)
        result.push(fst(tupleVal))
        maybe = snd(tupleVal)
        if (isNothing(maybe)): return result
        value = fromJust(maybe)

def unfoldr1ArrayImpl(isNothing):
    lambda fromJust: lambda fst: lambda snd: lambda f: lambda b: \
        _internalUnfolder(isNothing, fromJust, fst, snd, f, b)
