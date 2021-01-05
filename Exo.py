#importing an image with opencv
import cv2

#convert to black and white image
gray=cv2.imread('jon.jpg', 0) 

#display black and white image
cv2.imshow("BW", gray)
cv2.waitKey()
cv2.destroyAllWindows()

#save image
cv2.imwrite('jonBW.jpg', gray)

#new function
gray=cv2.split(gray)[0]
(retVal, newImg)=cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)

#display new image
cv2.imshow("new", newImg)
cv2.waitKey()
cv2.destroyAllWindows()

#save new image
cv2.imwrite('jonNew.jpg', newImg)
