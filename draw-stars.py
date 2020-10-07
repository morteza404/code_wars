"""
    author : morteza
    description : drawing below shape !

               *  
              ***
             *****
            *******

"""

# n is number of rows
def draw(n):
    for i in range(n):
        print( " " * ( n - (i + 1))  +  "*" * ( 2 * i + 1))

if __name__ == "__main__":
    # print(__doc__)
    draw(6)