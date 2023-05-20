import io
import pytesseract
import json
import io
from urllib import request as ur
from PIL import Image
import logging
import cv2
import numpy as np
import urllib.request

class Model:
    # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    def ocr(self, imgUrl):
        def img_process(img_url):
            req = urllib.request.urlopen(
                'https://firebasestorage.googleapis.com/v0/b/openeyes-59027.appspot.com/o/Original%2F1%2Fjyeon%2FIMG_3090.jpeg?alt=media&token=b7e766c1-8c3b-4dfe-9640-1605b69fa97c')
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1)

            cv2.imshow('test image', img)
            if cv2.waitKey() & 0xff == 27: quit()

            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            # threshold the image using Otsu
            thres=cv2.threshold(gray,0,255,
                               cv2.THRESH_OTSU)[1]
            cv2.imshow('Otsu',thres)
            text = str(pytesseract.image_to_string(thres, lang='kor+eng'))
            logging.debug(texts)
            return text
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
            # texts = img_open(imgUrl)
            texts = img_process(imgUrl)
        except Exception as e:
            texts=str(e)
            error_message = "Please check image contains text"

        context = {
            'text': texts,
            'error_message': error_message
        }
        return context

M=Model()
t=M.ocr('https://marketplace.canva.com/EAD1NDryb-o/1/0/1236w/canva-%EA%B8%88%EC%83%89-%EB%B0%9C%EB%A0%8C%ED%83%80%EC%9D%B8%EB%8D%B0%EC%9D%B4-%EC%9D%8C%EC%8B%9D-%EB%B0%8F-%EC%9D%8C%EB%A3%8C-%EB%A9%94%EB%89%B4-12JNKISfRrc.jpg')