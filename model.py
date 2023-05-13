import io
import pytesseract
import json
import io
from urllib import request as ur
from PIL import Image


class Model:
    def ocr(self, imgUrl):
        def img_open(img_url):
            res = ur.urlopen(img_url).read()
            f = io.BytesIO(res)
            img = Image.open(f)
            text = pytesseract.image_to_string(img, lang='kor+eng')
            return text

        text = ""
        error_message = ""
        try:
            text = img_open(imgUrl)
        except:
            error_message = "Please check image contains text"
        context = {
            'text': text,
            'error_message': error_message
        }
        return context
