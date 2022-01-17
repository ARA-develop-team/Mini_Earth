from matplotlib import pyplot as plt
# from matplotlib import pylab
import numpy as np


def show_graph(data):
    # plt.plot(data)

    plt.plot([2, 2, 3])
    plt.show()


def three_d():
    ax = plt.axes(projection='3d')
    # x_data = np.random.randint(0, 100, (500,))
    # y_data = np.random.randint(0, 100, (500,))
    # z_data = np.random.randint(0, 100, (500,))
    x = []
    y = []
    for i in range(100):
        x.append(i)
        y.append(i)
    X, Y, Z = np.meshgrid(x, y, my_list)

    ax.plot_surface(X, Y, Z)

    plt.show()


if __name__ == '__main__':
    # show_graph([3, 3, 10, 10])

    three_d()

