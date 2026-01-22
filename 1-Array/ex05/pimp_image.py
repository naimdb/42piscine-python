import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array):
    """Inverts the color of the image received."""
    inverted_array = array.copy()
    inverted_array[..., :3] = 255 - inverted_array[..., :3]
    plt.imshow(inverted_array.astype(np.uint8))
    plt.show()
    return inverted_array


def ft_red(array):
    """Keeps only the red channel of the image."""
    red_array = array.copy()
    red_array[..., 1] = 0
    red_array[..., 2] = 0
    plt.imshow(red_array.astype(np.uint8))
    plt.show()
    return red_array


def ft_green(array):
    """Keeps only the green channel of the image."""
    green_array = array.copy()
    green_array[..., 0] = 0
    green_array[..., 2] = 0
    plt.imshow(green_array.astype(np.uint8))
    plt.show()
    return green_array


def ft_blue(array):
    """Keeps only the blue channel of the image."""
    blue_array = array.copy()
    blue_array[..., 0] = 0
    blue_array[..., 1] = 0
    plt.imshow(blue_array.astype(np.uint8))
    plt.show()
    return blue_array


def ft_grey(array):
    """Converts the image to greyscale."""
    grey_array = array.copy()
    grey_values = np.dot(
        grey_array[..., :3], [0.2989, 0.5870, 0.1140]
    ).astype(np.uint8)
    grey_array[..., 0] = grey_values
    grey_array[..., 1] = grey_values
    grey_array[..., 2] = grey_values
    plt.imshow(grey_array.astype(np.uint8))
    plt.show()
    return grey_array
