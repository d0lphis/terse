# coding=utf-8

# [requirement]
# pip install pillow
# pip install pytesseract
# apt install tesseract-ocr
# go to https://github.com/tesseract-ocr/tessdata/, download eng.traineddata chi_sim.traineddata to /usr/share/tesseract-ocr/4.00/tessdata/

# [usage]
# python img2txt.py a.jpg



from PIL import Image
import pytesseract

image = Image.open('/home/stela/Desktop/video_to_image/6a9f014969739077de7aad80c08404f1/295.jpg')
print(image.size)
text = pytesseract.image_to_string(image, lang='chi_sim')
text = text.replace(" ", "")
print(text)
