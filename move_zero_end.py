"""

Moving Zeros To The End

5 kyu

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]

"""

s = [False,1,0,1,2,0,1,3,"a"]

out = []

for i in str(s):
    if i is "0" :
        out.append(i)
    
b = [i for i in s if i not in out] 

b.extend(out)

print(b)


