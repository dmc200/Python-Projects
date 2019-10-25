import random

# specify the number of times you want to flip with n as a parameter.


def randomHeadCount(n):
    heads = 0
    for i in range(0, n):
        num = random.randint(0,1)
        if num == 1:
            heads += 1
        if i == (n/2):
            print(f"Half way there! heads is at: {heads}")
           
    return heads

count = randomHeadCount(1000)
print(count)
