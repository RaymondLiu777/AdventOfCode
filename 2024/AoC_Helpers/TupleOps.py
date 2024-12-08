class TupleOps:
    def Add(tup1, *argv):
        value = tup1
        for arg in argv:
            value = tuple(map(lambda i, j: i + j, value, arg))
        return value
    
    def Subtract(tup1, tup2):
        return tuple(map(lambda i, j: i - j, tup1, tup2))

    def Multiply(tup1, multiple):
        return tuple(map(lambda i: i * multiple, tup1))

    def Neg(tup1):
        return tuple(map(lambda i: i * -1, tup1))