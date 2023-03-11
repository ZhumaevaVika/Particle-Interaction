import numpy as np
import matplotlib
from matplotlib import pyplot as plt


def show_histogram(vx_array):
    plt.hist(vx_array, bins = 20, density=True)
    plt.show()
        