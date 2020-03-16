def _internalUnfolder(isNothing, fromJust, fst, snd, f, b):
    result = []
    value = b
    while True:
        tupleVal = f(value)
        result.append(fst(tupleVal))
        maybe = snd(tupleVal)
        if isNothing(maybe):
            return result
        value = fromJust(maybe)


def unfoldr1ArrayImpl(isNothing):
    return lambda fromJust: lambda fst: lambda snd: lambda f: lambda b: _internalUnfolder(
        isNothing, fromJust, fst, snd, f, b
    )
