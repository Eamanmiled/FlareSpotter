import cv2 as cv

flarePhoto = cv.imread("images/four_flares.jpg")

grayPhoto = cv.cvtColor(flarePhoto, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(grayPhoto, 253, 255, cv.THRESH_BINARY)

#where the brigh stuff is
contour, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Draw red rectangles around detected bright spots
for c in contour:
    x, y, w, h = cv.boundingRect(c)
    if w > 2 and h > 2:  # ignore tiny noise
        cv.rectangle(flarePhoto, (x, y), (x + w, y + h), (0, 0, 255), 2)


cv.imshow("Light Sources Detected", flarePhoto)
cv.waitKey(10000)
cv.destroyAllWindows()

