class TupleOps:
    def Add(tup1, *argv):
        value = tup1
        for arg in argv:
            value = tuple(map(lambda i, j: i + j, value, arg))
        return value

    def Multiply(tup1, multiple):
        return tuple(map(lambda i: i * multiple, tup1))