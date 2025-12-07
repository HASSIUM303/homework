
import random

def random_integer(min_val, max_val):
    return random.randint(min_val, max_val)

def random_list(num_elements, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(num_elements)]

def shuffle_list(lst):
    shuffled = list(lst)
    random.shuffle(shuffled)
    return shuffled
