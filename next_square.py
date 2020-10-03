import math

def find_next_square(a):
    sq = math.sqrt(a)
    if pow(int(sq),2) == a :
        return int(pow(sq+1,2))
    return -1

print(find_next_square(121))