import numpy as np
from sklearn.decomposition import PCA
from PIL import Image

def compress_image(image_path, output_path, n_components):
    image = Image.open(image_path)
    image = image.convert('L')
    image_array = np.array(image)
    pca = PCA(n_components=n_components)
    compressed_image = pca.fit_transform(image_array)
    compressed_image = pca.inverse_transform(compressed_image)
    compressed_image = np.clip(compressed_image, 0, 255)
    compressed_image = Image.fromarray(compressed_image.astype('uint8'))
    compressed_image.save(output_path)

input_image_path = "C:\\5 AIML lab\\MML\\download.jpg"
output_image_path = "C:\\5 AIML lab\\MML\\download2.jpg"
num_components = 50

compress_image(input_image_path, output_image_path, num_components)