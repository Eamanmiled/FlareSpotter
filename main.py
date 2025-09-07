import cv2 as cv

flarePhoto = cv.imread("images/four_flares.jpg")

grayPhoto = cv.cvtColor(flarePhoto, cv.COLOR_BGR2GRAY)

cv.imshow("gray image", grayPhoto)

cv.waitKey(10000)
cv.destroyAllWindows()


