import random

def lineGrab():
    random_lines = random.choice(open(r"pwlist.txt").readlines())
    pudding = random_lines.strip()
    return pudding

def pwOutput():
    gen = [lineGrab(), lineGrab()]
    au = ''.join(gen)
    nums = random.randint(1000,9999)

    return(str(au) + str(nums) + '!')

pwOutput()
