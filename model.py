import io
import pytesseract
import json
import io
from urllib import request as ur
from PIL import Image
import logging

class Model:
    # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    def ocr(self, imgUrl):
        def img_open(img_url):
            text = "222"
            res = ur.urlopen(img_url).read()
            f = io.BytesIO(res)
            img = Image.open(f)
            text = str(pytesseract.image_to_string(img, lang='kor+eng'))
            logging.debug(texts)
            return text

        texts = ""
        error_message = ""

        try:
            texts = img_open(imgUrl)
        except Exception as e:
            texts=str(e)
            error_message = "Please check image contains text"

        context = {
            'text': texts,
            'error_message': error_message
        }
        return context
