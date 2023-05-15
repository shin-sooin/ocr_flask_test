import io
import pytesseract
import json
import io
from urllib import request as ur
from PIL import Image
import logging
import pyocr
import pyocr.builders
import numpy as np
class Model:
    # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    # def ocr(self, imgUrl):
    #     def img_open(img_url):
    #         text = "222"
    #         res = ur.urlopen(img_url).read()
    #         f = io.BytesIO(res)
    #         img = Image.open(f)
    #         text = str(pytesseract.image_to_string(img, lang='kor+eng'))
    #         logging.debug(texts)
    #         return text
    #
    #     texts = ""
    #     error_message = ""
    #
    #     try:
    #         texts = img_open(imgUrl)
    #     except Exception as e:
    #         texts=str(e)
    #         error_message = "Please check image contains text"
    #
    #     context = {
    #         'text': texts,
    #         'error_message': error_message
    #     }
    #     return context
    # Please downgrade cv2 before running the code
    # pip install opencv-python==4.5.5.64

    # import sys
    # import os
    # import pyocr
    # import pyocr.builders
    # import numpy as np
    # import urllib.request as ur
    # import io
    # import cv2
    # from PIL import Image
    # def train_model(trainset):
    #
    #     # Set up OCR engine
    #     tools = pyocr.get_available_tools()
    #     if len(tools) == 0:
    #         print("No OCR tool found")
    #         sys.exit(1)
    #     ocr_tool = tools[0]
    #
    #     # Load training data
    #     data = []
    #     labels = []
    #     for i in range(10):  # assuming 10 classes
    #         for j in range(50):  # assuming 50 samples per class
    #             img = Image.open(f"training_data/{i}_{j}.png")
    #             data.append(np.array(img))
    #             labels.append(i)
    #
    #     # Train model
    #     ocr_tool.train(np.array(data), np.array(labels))
    #
    #     # Save model
    #     ocr_tool.save("my_ocr_model")

    def img_open(imgUrl):
        res = ur.urlopen(imgUrl).read()
        # open image
        f = io.BytesIO(res)
        img = Image.open(f)
        return img

    def ocr(self, imgUrl):
        text = ""
        error_message = ""
        # open image through imgUrl
        try:
            res = ur.urlopen(imgUrl).read()
            # open image
            f = io.BytesIO(res)
            img = Image.open(f)
        except:
            error_message = 'please check url of image.'

        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print('OCR tool is not found')
            # sys.exit(1)
            return 'loading ocr tool error'
        tool = tools[0]
        wk_builder = pyocr.builders.WordBoxBuilder()
        ocr_results = tool.image_to_string(
            img,
            lang='kor+eng',
            builder=wk_builder
        )

        editor = []
        before_position = 0
        for ocr_result in ocr_results:
            # print position
            print(ocr_result.position)
            if ocr_result.position[1][1] - before_position > 30:
                before_position = ocr_result.position[1][1]
                editor.append('\n')
            editor.append(ocr_result.content)
            # cv2.rectangle(img, ocr_result.position[0], ocr_result.position[1],(0,255,255),1)

        context = {
            'text': editor,
            'error_message': error_message,
            # 'request_img': request_img,
            # 'summarized_text': summarized_text
        }
        return context
