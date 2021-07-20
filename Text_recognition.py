import cv2
import pytesseract

## path to tesseract engine
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

##importing image
img = cv2.imread('Skill.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # Rescaling of the image
# # INTER_CUBIC is used to enlarge for recognizing small characters
# img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# # INTER_AREA is used to shrink an image
# img = cv2.resize(img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
# # INTER_LINEAR is used to faster performance by reducing the image quality
# img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# #blurring and filtering
# #Averaging
# img = cv2.blur(img,(5,5))
# # Bilateral filtering
# img = cv2.bilateralFilter(img,2,50,50)
# # Gaussian blurring
# img = cv2.gaussianblur(img (5, 5), 0)
# # Median blurring
# img = cv2.medianBlur(img, 3)

# # to convert into gray image
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # to get binary image
# img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

## to read the text
# For language other than English put first three letters of lnguage
config = "--psm 4"
print(pytesseract.image_to_string(img, config=config, lang='eng'))

print( img.shape )
boxes = (pytesseract.image_to_boxes(img))

## to show the image
cv2.imshow('Result', img)

##to keep image open
cv2.waitKey(0)
