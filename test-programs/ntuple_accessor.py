from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = PublicInteger(Input(name="my_int1", party=party1))
    my_int2 = PublicInteger(Input(name="my_int2", party=party1))

    array = Array.new(my_int1, my_int1)

    # Store a scalar, a compound type and a literal.
    tuple = NTuple.new([my_int1, array, Integer(42)])

    scalar = tuple[0]
    array = tuple[1]
    literal = tuple[2]

    @nada_fn
    def add(a: PublicInteger) -> PublicInteger:
        return a + my_int2

    sum = array.reduce(add, Integer(0))

    return [Output(scalar + literal + sum, "my_output", party1)]
