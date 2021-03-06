import numpy as np
import matplotlib.pyplot as plt

for index in range(751):
    filename = f"./data/output_{index}.dat"

    output = np.loadtxt(filename, unpack=True)

    fig = plt.figure(figsize=(6, 3.2))

    ax = fig.add_subplot(111)
    ax.set_title('Video of implementation of wave equation')
    plt.imshow(output)
    ax.set_aspect('equal')

    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation='vertical')

    fig.savefig(f"images/frame_{index}.png", dpi=fig.dpi)
