import numpy as np
from PIL import Image
from a2_ex1 import to_grayscale
import math

# prepare_image -> tuple[np.ndarray, np.ndarray]
def prepare_image(image: np.ndarray,
                  width: int,
                  height: int,
                  x: int,
                  y: int,
                  size: int):
    # 1, 1280, 960
    #Checks
    if image.shape[0] != 1 or image.ndim != 3:
        raise ValueError
    if width < 32 or height < 32 or size < 32:
        raise ValueError
    if width < x + size or x < 0:
        raise ValueError
    if height < y + size or y < 0:
        raise ValueError
    
    resized = image

    #resizing image
    if height > image.shape[1]:
        #equaly adding pixels to the top and bottom
        resized = np.pad(resized, pad_width=((0,0), (math.floor(height/2), math.ceil(height/2)), (0,0)), mode="edge")
    if width > image.shape[2]:
        #equaly adding pixels to the left and right
        resized = np.pad(resized, pad_width=((0,0), (0,0), (math.floor(width/2), math.ceil(width/2))), mode="edge")
    else:
        resized = resized[:, 
                    math.ceil((image.shape[1]-height)/2):math.ceil((image.shape[1]-height)/2)+height, 
                    math.ceil((image.shape[2]-width)/2):math.ceil((image.shape[2]-width)/2)+width]
    
    #finding subarea
    subarea = resized
    subarea = subarea[:, y:y+size, x:x+size]

    return (resized, subarea)

    

#TEST, REMOVE BEFORE SUBMITING
from matplotlib import pyplot as plt
img = Image.open("./book.jpg")
numpy_array = np.array(img)
array = to_grayscale(numpy_array)
image = prepare_image(array, 500, 500, 30, 30, 100)[1]

image = image.reshape((image.shape[1], image.shape[2], image.shape[0]))

plt.imshow(image, cmap='gray')
plt.savefig('img.png')