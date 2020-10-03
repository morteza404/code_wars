"""
     *
    ***
   *****
  ******* 
 *********
***********

"""

out = []

for i in range(6):
    for j in range(11):
        out[i][(j//2)+1] = "*"
print(out)