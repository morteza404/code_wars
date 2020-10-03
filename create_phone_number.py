a = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0] # => returns "(123) 456-7890"



def create_phone_number(a):

    a1 = ""

    for i in a:
        a1 += str(i)

    return f"({a1[0:3]}) {a1[3:6]}-{a1[6:]}"


print(create_phone_number(a))

