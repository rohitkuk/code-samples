images = [] # Put images as numpy arrays in this list

import numpy as np
from IPython.display import HTML
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm
matplotlib.rcParams['animation.embed_limit'] = 2**64
fig = plt.figure(figsize=(8,8))
plt.axis("off")
ims = []


from matplotlib import animation
for j,i in tqdm(enumerate(images)):
    ims.append([plt.imshow(np.transpose(i,(1,2,0)), animated=True)]) 
    

ani = animation.ArtistAnimation(fig, ims, interval=1000, repeat_delay=1000, blit=True)
HTML(ani.to_jshtml())
f = "animation{}.gif".format(datetime.datetime.now()).replace(":","")

from matplotlib.animation import PillowWriter

ani.save(f, writer=PillowWriter(fps=20)) 
