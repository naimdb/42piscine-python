import numpy as np
from PIL import Image
import os


def ft_load(path: str):
    """
    Load an image and return it as a numpy array.

    Args:
        path: Path to the image file (JPG/JPEG)

    Returns:
        numpy array of the image in RGB format

    Raises:
        AssertionError: If file not found or invalid format
    """
    try:
        if not isinstance(path, str):
            raise AssertionError("Error: path must be a string")

        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError(
                "Error: only JPG and JPEG formats are supported"
            )

        if not os.path.exists(path):
            raise AssertionError(f"Error: file not found: {path}")

        img = Image.open(path)

        array = np.array(img)

        print(f"The shape of image is: {array.shape}")
        print(array)

        return array

    except AssertionError:
        raise
    except FileNotFoundError:
        raise AssertionError(f"Error: file not found: {path}")
    except Exception as e:
        raise AssertionError(f"Error: cannot load image: {e}")
