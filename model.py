import io
import pytesseract
import json
import io
from urllib import request as ur
from PIL import Image
import logging

class Model:

    def ocr(self, imgUrl):
        # def img_open(img_url):
        #     texts = "222"
        #     res = ur.urlopen(img_url).read()
        #     f = io.BytesIO(res)
        #     img = Image.open(f)
        #     texts = str(pytesseract.image_to_string(img, lang='kor+eng'))
        #     logging.debug(texts)
        #     return texts

        texts = ""
        error_message = ""

        try:
            # texts = img_open(imgUrl)
            texts = "222"
            res = ur.urlopen(imgUrl).read()
            f = io.BytesIO(res)
            img = Image.open(f)
            texts = str(pytesseract.image_to_string(img, lang='kor+eng'))
            logging.debug(texts)
        except:
            error_message = "Please check image contains text"
        context = {
            'text': texts,
            'error_message': error_message
        }
        return context
