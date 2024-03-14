import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
# Load the image
img = plt.imread(r"C:\Users\sujan\Downloads\CYLI.jpeg")
# Convert the image into a two-dimensional array
img_2d = img.reshape(img.shape[0], img.shape[1] * img.shape[2])
# Apply PCA to the two-dimensional array to compress the image
pca = PCA(n_components=500)
img_pca = pca.fit_transform(img_2d)
# Reconstruct the compressed image
img_reconstructed = pca.inverse_transform(img_pca)
# Display the reconstructed image
plt.imshow(img_reconstructed.reshape(img.shape))
plt.title('Reconstructed Image')
plt.savefig('new.jpg')
plt.show()