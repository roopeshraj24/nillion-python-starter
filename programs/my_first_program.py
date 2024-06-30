from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the difference and quotient of my_int1 and my_int2
    difference_result = my_int1 - my_int2
    quotient_result = my_int1 / my_int2

    # Return the difference and quotient as outputs
    return [
        Output(difference_result, "difference_output", party1),
        Output(quotient_result, "quotient_output", party1)
    ]
