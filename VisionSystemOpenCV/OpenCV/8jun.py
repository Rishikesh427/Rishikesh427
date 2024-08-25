import cv2

# Define function to calculate Mean Squared Error (MSE)
def mse(image1, image2):

  # Calculates the Mean Squared Error between two images.

  # Arguments:
  #     image1: First image
  #     image2: Second image

  # Returns:
  #     The MSE value between the two images.

  diff = image1.astype("float") - image2.astype("float")
  return cv2.mean(diff ** 2)[0]

# Load images
image1 = cv2.imread("image1.png")
image2 = cv2.imread("image2.png")

# Convert to grayscale
image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Calculate MSE
mse_value = mse(image1_gray, image2_gray)

# Define threshold for similarity
threshold = 1100

# Determine similarity
if mse_value < threshold:
  print("Images are similar.")
else:
  print("Images are different.")

# Display images (optional)
# cv2.imshow("Image 1", image1)
# cv2.imshow("Image 2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
