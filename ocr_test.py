import pytesseract
import urllib.request
import cv2
import numpy as np
import imutils
from imutils.perspective import four_point_transform
import re
import requests

def img_process(img_url):
    import pytesseract
    import urllib.request
    import cv2
    import numpy as np
    import imutils

    import re
    import requests
    req = urllib.request.urlopen(img_url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)

    # convert image to grayscale
    image = imutils.resize(img, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
    edged = cv2.Canny(blurred, 75, 200)

    # resize & denoise image
    denoised = cv2.fastNlMeansDenoising(gray, h=10, searchWindowSize=21, templateWindowSize=7)
    res, thresh = cv2.threshold(denoised, 196, 255, cv2.THRESH_BINARY)

    # thresh[260:2090]=~thresh[260:2090]
    result = np.hstack((gray, thresh))
    # cv2.imshow(result)
    #
    # cv2.imshow(image)
    # cv2.imshow(gray)
    # cv2.imshow(blurred)
    # cv2.imshow(edged)

    text = str(pytesseract.image_to_string(image, lang='kor'))
    text2 = str(pytesseract.image_to_string(edged, lang='kor'))
    text3 = str(pytesseract.image_to_string(gray, lang='kor'))
    text4 = str(pytesseract.image_to_string(blurred, lang='kor'))
    text5 = str(pytesseract.image_to_string(result, lang='kor+eng'))
    # print(pytesseract.image_to_boxes(image))
    print('text5: ', text5)

    return text, text2, text3, text4, text5

temp_original, temp_edged, temp_gray, temp_blurred, temp_denoised=img_process('https://www.safetimes.co.kr/news/photo/201912/78752_54867_1338.jpg')
# temp_edged, temp_gray, temp_blurred, temp_original=img_process('/content/33AED5DA-F666-463B-8ED3-1AA7DB06F5B1 (1).jpg')
print('original','--------'*5)
print(temp_original)
print('edged','--------'*5)
print(temp_edged)
print('gray','--------'*5)
print(temp_gray)
print('blurred','--------'*5)
print(temp_blurred)
print('denoise&threshold','--------'*5)
print(temp_denoised)