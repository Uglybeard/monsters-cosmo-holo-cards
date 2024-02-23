import os
import random
import string

os.chdir("./utility")
for i in range(1,42):
    str =  ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(6))
    os.makedirs(os.path.join("./", str))
    os.chdir("./" + str)
    with open("./t_" + ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(3)) + ".txt","w") as f:
        f.write(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(38)))

