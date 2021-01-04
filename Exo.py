#importing an image with opencv
import cv2

#read image in color
image=cv2.imread('jon.jpg')

#convert to black and white image
gray=cv2.imread('jon.jpg', 0) 

#display black and white image
cv2.imshow("BW", gray)
cv2.waitKey()
cv2.destroyAllWindows()

#save image
cv2.imwrite('jonBW.jpg', gray)
