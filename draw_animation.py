import itertools

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



def update(data, save_name):
    update_interval = 50
    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])
    img = ax.imshow(data, cmap='autumn', interpolation='nearest')
    ani = animation.FuncAnimation(fig, generate, fargs=(img, plt, data),
                                  frames=20,
                                  interval=update_interval,
                                  save_count=50)
    if save_name:
        ani.save(save_name, fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()