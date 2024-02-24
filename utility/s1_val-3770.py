import os
import random
import string

chars = ['A', 'E', 'H', 'I', 'L', 'O', 'P', 'S', 'T', 'U', 'V', 'Z']
ls = [7, 3, 10, 0, 4, 4, 1, 8, 8, 5, 2, 6, 5, 4, 3, 11, 3, 0, 0, 0]
    
os.chdir("./utility")

for i in range(0,20):
    str =  chars[ls[i]] + "".join(random.choice(string.digits) for i in range(6))
    os.makedirs(os.path.join("./", str))
    os.chdir("./" + str)
    with open("./t_" + ''.join(random.choice(string.ascii_letters) for i in range(3)) + ".txt","w") as f:
        f.write(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(38)))

