from PIL import Image
import matplotlib.pyplot as plt
from operations import *

# Function to plot original and processed images
def plot_images(original_image, processed_image, function_name):
    plt.figure(figsize=(10, 5))

    # Plot original image
    plt.subplot(1, 2, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Original Image')

    # Plot processed image
    plt.subplot(1, 2, 2)
    plt.imshow(processed_image, cmap='gray')
    plt.title(f'Processed Image ({function_name})')

    plt.tight_layout()
    plt.show()

# Example usage
image_path = 'Images\images - Copy.jpeg'  # Image path from your code
original_image = Image.open(image_path)
processed_image = detect_edges(image_path)  # Function name from your code, replace with your desired function
plot_images(original_image, processed_image, 'Detect Edges')  # Function name from your code
