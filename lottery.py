import random

def generate_output():
    # using random.sample to sample 10 numbers without repetition
    drawn_balls = random.sample(range(1, 50), 10)
    return sorted(drawn_balls)
