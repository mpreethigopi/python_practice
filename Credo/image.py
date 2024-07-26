import cv2
from matplotlib import pyplot as plt

image=cv2.imread("G:/IMG_3028.jpg")
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inverted=255-gray_image
blur=cv2.GaussianBlur(inverted,(21,21),0)
invertedblur=255-blur
sketch=cv2.divide(gray_image, invertedblur, scale=256.0)
#cv2.imwrite("sketch_image.png", sketch)
"""cv2.imshow("sketch Image", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
"""plt.imshow(sketch, cmap='gray')
plt.title('Sketch Image')
plt.axis('off')  # Hide axes
plt.show()"""

darkening_factor = 0.5
dark_sketch = cv2.multiply(sketch, darkening_factor)
    
    # Save the darkened sketch image
cv2.imwrite("dark_sketch_image.png", dark_sketch)
    
    # Display the darkened sketch image using matplotlib
plt.imshow(dark_sketch, cmap='gray')
plt.title('Dark Sketch Image')
plt.axis('off')  # Hide axes
plt.show()