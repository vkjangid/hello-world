# abstaction
import random


class RandNumber:
    __rng_no = 0

    def __get_no(numb):
        return random.randrange(numb)

    def get_random_no(numb):
        RandNumber.__rng_no = RandNumber.__get_no(numb)
        return RandNumber.__rng_no
