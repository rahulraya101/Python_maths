import os
import random
import dircache

dir = 'some/directory'
filename = random.choice(dircache.listdir(dir))
path = os.path.join(dir, filename)
