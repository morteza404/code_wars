
def is_prime(num): 
    if num > 1:          
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
             


for item in range(100):
    if is_prime(item):
        print(item)