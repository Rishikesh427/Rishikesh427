import time
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture")

count = 0

while count <= 2:
# Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")

    # Display the frame
    cv.imshow('Frame', frame)

    # Save the frame as an image file
    filename = f"image{count}.jpg"
    cv.imwrite(filename, frame)
    print(f"Saved {filename}")

    count += 1

    time.sleep(1)
    # Wait for a key press for a short period (e.g., 100 ms)
    # Press 'q' to quit early
    if cv.waitKey(100) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()