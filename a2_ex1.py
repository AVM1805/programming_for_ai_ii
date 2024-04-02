from PIL import Image
import numpy as np

#to_grayscale(pil_image: np.ndarray) -> np.ndarray
def to_grayscale(pil_image: np.ndarray):
    if pil_image.ndim == 2:
        return pil_image.reshape((1, pil_image.shape[0], pil_image.shape[1]))
    if pil_image.ndim != 3:
        raise ValueError
    if pil_image.shape[2] != 3:
        raise ValueError
    
    normalised_image = pil_image / 255

    C_linear = np.where(normalised_image<=0.04045, normalised_image/12.92, ((normalised_image+0.055)/1.055)**2.4)
    
    Y_linear = np.sum(C_linear*np.array([0.2126, 0.7152, 0.0722]), axis=-1)

    Y = np.where(Y_linear<=0.0031308, 12.92*Y_linear, 1.055*Y_linear**(1/2.4) - 0.055)

    reshaped_image = Y.reshape((1, Y.shape[0], Y.shape[1]))

    if np.issubdtype(pil_image.dtype, np.integer):
        return reshaped_image.round(0).astype(pil_image.dtype)
    return reshaped_image.astype(pil_image.dtype)


#TEST, REMOVE BEFORE SUBMITING
# from matplotlib import pyplot as plt
# img = Image.open("./book.jpg")
# numpy_array = np.array(img)
# array = to_grayscale(numpy_array)
# plt.imshow(array.reshape((array.shape[1], array.shape[2], 1)), cmap='gray')
# plt.savefig('img.png')
