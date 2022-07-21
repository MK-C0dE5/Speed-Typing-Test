import random
def random_line(sentances):
    lines = open(sentances).read().splitlines()
    return random.choice(lines)
print(random_line('sentences.txt'))
