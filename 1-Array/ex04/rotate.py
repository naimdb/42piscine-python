import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():

    new_array = ft_load("animal.jpeg")

    img_zoom = np.dot(new_array[..., :3], [0.2989, 0.5870, 0.1140])
    img_zoom = img_zoom[..., np.newaxis].round().astype(int)

    h, w = 400, 400
    center_h, center_w = img_zoom.shape[0] // 2, img_zoom.shape[1] // 2
    img_zoom = img_zoom[center_h - h//2:center_h + h//2,
                        center_w - w//2:center_w + w//2]

    print(f"The shape of image is: {img_zoom.shape}")
    print(img_zoom)

    img_rotate = np.zeros((img_zoom.shape[1], img_zoom.shape[0],
                           img_zoom.shape[2]), dtype=img_zoom.dtype)
    for i in range(img_zoom.shape[0]):
        for j in range(img_zoom.shape[1]):
            img_rotate[j][i] = img_zoom[i][j]

    print(f"New shape after rotate: {img_rotate.shape}")
    print(img_rotate)

    plt.imshow(img_rotate, cmap='gray')
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
