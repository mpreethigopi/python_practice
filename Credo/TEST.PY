import cv2
from matplotlib import pyplot as plt

# Read the image from the specified path
image = cv2.imread("G:/CSN_5738.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or path is incorrect")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted = 255 - gray_image
    
    # Apply Gaussian blur to the inverted image
    blur = cv2.GaussianBlur(inverted, (21, 21), 0)
    
    # Invert the blurred image
    inverted_blur = 255 - blur
    
    # Create the sketch image using the divide function
    sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)
    
    # Darken the sketch by subtracting a constant value
    dark_sketch = cv2.subtract(sketch, 50)  # Subtract 50 from each pixel value
    
    # Ensure pixel values stay within valid range
    dark_sketch = cv2.max(dark_sketch, 0)  # Ensure no values below 0
    
    # Save the darkened sketch image
    cv2.imwrite("dark_sketch_image.png", dark_sketch)
    
    # Display the darkened sketch image using matplotlib
    plt.imshow(dark_sketch, cmap='gray')
    plt.title('Dark Sketch Image')
    plt.axis('off')  # Hide axes
    plt.show()
