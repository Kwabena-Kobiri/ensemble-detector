import cv2
import time

image = cv2.imread('../test images/fog.jpg')

cv2.imshow( "frame", image)

cv2.waitKey(0)
cv2.destroyAllWindows()